from PyPDF2 import PdfMerger

def merge_pdfs(input_files, output_file):
    merger = PdfMerger()
    
    for pdf in input_files:
        merger.append(pdf)
    
    merger.write(output_file)
    merger.close()
