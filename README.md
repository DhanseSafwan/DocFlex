# DocFlex - PDF Converter Web App

## 📌 Project Description
The **DocFlex - PDF Converter Web App** is a powerful and user-friendly tool that allows users to seamlessly convert, merge, split, and manage PDFs. It supports multiple file format conversions, making document processing easy and efficient.

## 🚀 Key Features
- **Merge PDFs** → Combine multiple PDF files into one.
- **Split PDFs** → Extract pages or split PDFs into smaller files.
- **PDF to Word** → Convert PDFs into editable DOCX files.
- **Word to PDF** → Convert DOCX documents into PDFs.
- **PDF to PowerPoint** → Convert PDFs into PPTX slides.
- **PowerPoint to PDF** → Convert PPTX slides into PDFs.
- **PDF to Excel** → Extract tables and data into XLSX format.
- **Excel to PDF** → Convert XLSX spreadsheets into PDFs.
- **Upcoming Features** → JPG to PDF, PDF to JPG, HTML to PDF, adding page numbers, and more!

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Libraries:** Flask, PyPDF2, pdf2docx, docx2pdf, pdfplumber, pandas, comtypes
- **Database:** (Not required for basic file conversion, but can be added for user management)

## 📂 Project Structure
```
Pdf_Converter/
│-- app.py                # Flask main application
│-- requirements.txt      # Dependencies list
│-- pdf_models/           # PDF processing scripts
│   │-- merge_pdf.py
│   │-- split_pdf.py
│   │-- pdf_word_converter.py
│-- static/               # Static files (CSS, Images)
│   │-- styles.css
│   │-- icons/
│-- templates/            # HTML templates
│   │-- index.html
│-- uploads/              # Directory to store uploaded files
```

## 🛠️ Installation & Setup
### 🔹 Prerequisites
- Python 3.x installed
- Pip package manager

### 🔹 Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/pdf-converter.git
   cd pdf-converter
   ```
2. **Create a Virtual Environment** *(optional but recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Flask App**
   ```bash
   python app.py
   ```
5. **Open the App in Browser**
   Visit: `http://127.0.0.1:5000/`

## 📷 Screenshots
Merging PDF's example.
![1](https://github.com/user-attachments/assets/f921d425-2c67-4c93-a426-c3ba4746f200)
![2 1](https://github.com/user-attachments/assets/6d2bd2f7-0959-4668-a1fc-35c171e125ec)
![3](https://github.com/user-attachments/assets/0f05c1dc-499c-4e86-93cd-e6f83ef5eec1)
![4](https://github.com/user-attachments/assets/244906a3-5514-4b2c-9541-ecfd545996fb)



## 🤝 Contributing
Feel free to fork this repository and submit pull requests with improvements! 🚀

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

