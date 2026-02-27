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

        runs = paragraph.runs

        for run_index, run in enumerate(runs):

            run_text = run.text

            matches = list(pattern.finditer(run_text))

            for match in matches:

                placeholder_text = match.group()

                placeholders.append({
                    "type": "run",
                    "paragraph_obj": paragraph,
                    "run_obj": run,
                    "run_index": run_index,
                    "placeholder": placeholder_text,
                    "start_in_run": match.start(),
                    "end_in_run": match.end(),
                    "full_run_text": run_text
                })

    return placeholders

