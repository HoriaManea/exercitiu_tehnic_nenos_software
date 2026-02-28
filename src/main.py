from load_document import load_document
from load_json import load_json
from find_placeholders import find_placeholders
from ai_agent import ai_agent_batch
from fill_doc import fill_doc


if __name__ == "__main__":
    doc_path = "output_forms.docx"
    json_path = "input_data.json"

    document = load_document(doc_path)

    data = load_json(json_path)

    placeholders = find_placeholders(document)

    if not placeholders:
        exit()

    paragraph_texts = [p["text"] for p in placeholders]

    batch_size = 20
    mapping = {}

    for i in range(0, len(paragraph_texts), batch_size):
        batch = paragraph_texts[i:i + batch_size]

        batch_mapping = ai_agent_batch(batch, list(data.keys()))

        for k, v in batch_mapping.items():
            try:
                original_index = i + int(k)
                mapping[str(original_index)] = v
            except:
                continue


    for index_str, matched_key in mapping.items():
        print("Trying to fill:", index_str, "->", matched_key)

        try:
            index = int(index_str)
        except ValueError:
            continue

        if matched_key in data:
            paragraph = placeholders[index]["paragraph"]
            value = data[matched_key]

            fill_doc(paragraph, value)
        else:
            print("Key not found in JSON:", matched_key)

    document.save("output_forms.filled.docx")