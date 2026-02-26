from docx import Document
from pathlib import Path

def load_document(path: str) -> Document:
    if not Path(path).exists():
        raise FileNotFoundError(f"File not found: {path}")
    return Document(path)

    
if __name__ == "__main__":
    doc_path = 'text_word.docx'
    document = load_document(doc_path)
    
    if document:
        print('documentul exista')
