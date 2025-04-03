import win32com.client

def excel_to_pdf(excel_file, pdf_file):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False
    workbook = excel.Workbooks.Open(excel_file)

    workbook.ExportAsFixedFormat(0, pdf_file)  # 0 = PDF format
    workbook.Close()
    excel.Quit()
