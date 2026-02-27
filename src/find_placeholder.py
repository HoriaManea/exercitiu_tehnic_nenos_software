import re
from extract_table_paragraphs import extract_table_paragraphs
from docx import Document

def find_placeholders(document: Document):
    placeholders = []

    pattern = re.compile(r"[_\.]{3,}")  

    all_paragraphs = []

    all_paragraphs.extend(document.paragraphs)

    for table in document.tables:
        all_paragraphs.extend(extract_table_paragraphs(table))

    for section in document.sections:
        all_paragraphs.extend(section.header.paragraphs)
        all_paragraphs.extend(section.footer.paragraphs)

        for table in section.header.tables:
            all_paragraphs.extend(extract_table_paragraphs(table))

        for table in section.footer.tables:
            all_paragraphs.extend(extract_table_paragraphs(table))
        


    for paragraph in all_paragraphs:
        fulltext = paragraph.text

        for match in pattern.finditer(fulltext):
            placeholder_text = match.group()

            placeholders.append({
                "type": "paragraph",
                # "index": i,
                "paragraph_obj": paragraph,   
                "text": fulltext,
                "placeholder": placeholder_text,
                # "label": label
            })
            print(match.start())
            print(match.end())

    return placeholders

