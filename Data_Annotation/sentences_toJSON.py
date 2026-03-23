import json

input_file = "sentences.txt"
output_file = "JSONsentences.json"

data = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        text = line.strip()
        if text:
            data.append({"text": text})

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done! File saved as JSONsentences.json")