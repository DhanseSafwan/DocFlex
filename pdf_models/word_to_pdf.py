from docx2pdf import convert

def word_to_pdf(word_file, pdf_file):
    convert(word_file, pdf_file)
