from pdf2docx import Converter

def pdf_to_ppt(pdf_file, ppt_file):
    cv = Converter(pdf_file)
    cv.convert(ppt_file, start=0, end=None)
    cv.close()
