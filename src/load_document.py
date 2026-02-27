from docx import Document
from pathlib import Path

def load_document(path: str) -> Document:
    if not Path(path).exists():
        raise FileNotFoundError(f"File not found: {path}")
    return Document(path)