from load_document import load_document
from find_placeholder import find_placeholders


if __name__ == "__main__":
    doc_path = "output_forms.docx"
    document = load_document(doc_path)

    placeholders = find_placeholders(document)

    # for p in placeholders:
        # print({
        #     "label": p["label"],
        #     "placeholder": p["placeholder"]
        # })