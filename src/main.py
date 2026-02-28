from load_document import load_document
from find_placeholders import find_placeholders


if __name__ == "__main__":
    doc_path = "output_forms.docx"
    document = load_document(doc_path)

    placeholders = find_placeholders(document)

    print(len(document.paragraphs))
    print(len(document.tables))
    print(len(placeholders))