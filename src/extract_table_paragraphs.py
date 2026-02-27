def extract_table_paragraphs(table):
    paragraphs = []

    for row in table.rows:
        for cell in row.cells:
            paragraphs.extend(cell.paragraphs)

            for inner_table in cell.tables:
                paragraphs.extend(extract_table_paragraphs(inner_table))

    return paragraphs