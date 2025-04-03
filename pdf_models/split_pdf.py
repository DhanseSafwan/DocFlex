from PyPDF2 import PdfReader, PdfWriter

def split_pdfs(input_file, output_folder):
    reader = PdfReader(input_file)
    
    for i in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        
        output_file = f"{output_folder}/page_{i+1}.pdf"
        with open(output_file, "wb") as f:
            writer.write(f)
