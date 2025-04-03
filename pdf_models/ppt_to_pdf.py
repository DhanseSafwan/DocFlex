import comtypes.client

def ppt_to_pdf(ppt_file, pdf_file):
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1

    presentation = powerpoint.Presentations.Open(ppt_file)
    presentation.SaveAs(pdf_file, 32)  # 32 = PDF format
    presentation.Close()
    powerpoint.Quit()
