from docx import Document
from pathlib import Path

def load_document(path: str):
    if not Path(path).exists():
        print("nu exista")
        return
    
    doc = Document(path)
    print("document incarcat")
    return doc

load_document('text_word.docx')