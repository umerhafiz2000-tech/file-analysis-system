from docx import Document
from PyPDF2 import PdfReader

def load_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def load_pdf(path):
    reader = PdfReader(path)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
