import pdfplumber
import pandas as pd

def pdf_to_excel(pdf_file, excel_file):
    with pdfplumber.open(pdf_file) as pdf:
        tables = [page.extract_table() for page in pdf.pages]

    df = pd.DataFrame([row for table in tables if table for row in table])
    df.to_excel(excel_file, index=False)
