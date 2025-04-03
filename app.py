from flask import Flask, render_template, request, send_file
import os

from pdf_models.merge_pdf import merge_pdfs
from pdf_models.split_pdf import split_pdfs
from pdf_models.pdf_to_word import pdf_to_word
from pdf_models.word_to_pdf import word_to_pdf
from pdf_models.pdf_to_ppt import pdf_to_ppt
from pdf_models.ppt_to_pdf import ppt_to_pdf
from pdf_models.pdf_to_excel import pdf_to_excel
from pdf_models.excel_to_pdf import excel_to_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_pdf():
    files = request.files.getlist("files")
    file_paths = []

    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        file_paths.append(path)

    output_file = os.path.join(OUTPUT_FOLDER, "merged.pdf")
    merge_pdfs(file_paths, output_file)

    return send_file(output_file, as_attachment=True)

@app.route('/split', methods=['POST'])
def split_pdf():
    file = request.files["file"]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    split_pdfs(input_path, OUTPUT_FOLDER)

    return "PDF split successfully!"

@app.route('/pdf_to_word', methods=['POST'])
def convert_pdf_to_word():
    file = request.files["file"]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    output_file = os.path.join(OUTPUT_FOLDER, "converted.docx")
    pdf_to_word(input_path, output_file)

    return send_file(output_file, as_attachment=True)

@app.route('/word_to_pdf', methods=['POST'])
def convert_word_to_pdf():
    file = request.files["file"]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    output_file = os.path.join(OUTPUT_FOLDER, "converted.pdf")
    word_to_pdf(input_path, output_file)

    return send_file(output_file, as_attachment=True)

@app.route('/pdf_to_ppt', methods=['POST'])
def convert_pdf_to_ppt():
    file = request.files["file"]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    output_file = os.path.join(OUTPUT_FOLDER, "converted.pptx")
    pdf_to_ppt(input_path, output_file)

    return send_file(output_file, as_attachment=True)

@app.route('/ppt_to_pdf', methods=['POST'])
def convert_ppt_to_pdf():
    file = request.files["file"]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    output_file = os.path.join(OUTPUT_FOLDER, "converted.pdf")
    ppt_to_pdf(input_path, output_file)

    return send_file(output_file, as_attachment=True)

@app.route('/pdf_to_excel', methods=['POST'])
def convert_pdf_to_excel():
    file = request.files["file"]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    output_file = os.path.join(OUTPUT_FOLDER, "converted.xlsx")
    pdf_to_excel(input_path, output_file)

    return send_file(output_file, as_attachment=True)

@app.route('/excel_to_pdf', methods=['POST'])
def convert_excel_to_pdf():
    file = request.files["file"]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    output_file = os.path.join(OUTPUT_FOLDER, "converted.pdf")
    excel_to_pdf(input_path, output_file)

    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
