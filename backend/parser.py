# parser.py
import os
import io
from docx import Document
import pdfplumber


ALLOWED = {'pdf', 'docx', 'txt'}


def allowed_file(filename):
return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED




def parse_docx(path):
doc = Document(path)
texts = [p.text for p in doc.paragraphs if p.text]
return '\n'.join(texts)




def parse_pdf(path):
text_chunks = []
with pdfplumber.open(path) as pdf:
for page in pdf.pages:
t = page.extract_text()
if t:
text_chunks.append(t)
return '\n'.join(text_chunks)




def parse_txt(path):
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
return f.read()




def extract_text(path):
ext = path.rsplit('.', 1)[1].lower()
if ext == 'pdf':
return parse_pdf(path)
if ext == 'docx':
return parse_docx(path)
if ext == 'txt':
return parse_txt(path)
return ''
