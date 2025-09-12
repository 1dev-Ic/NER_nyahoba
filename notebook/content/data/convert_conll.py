import json

# Load your merged dataset
with open("merged_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

conll_lines = []

for task in data:
    text = task["data"]["text"]
    anns = task["annotations"][0]["result"] if task["annotations"] else []

    # Start with "O" for each token
    tokens = text.split()
    labels = ["O"] * len(tokens)

    for ann in anns:
        value = ann["value"]
        start = value["start"]
        end = value["end"]
        label = value["labels"][0]

        # Find which tokens are covered by this annotation
        covered = []
        running_index = 0
        for i, tok in enumerate(tokens):
            token_start = running_index
            token_end = running_index + len(tok)
            if token_end > start and token_start < end:
                covered.append(i)
            running_index = token_end + 1  # +1 for space

        # Assign BIO tags
        for j, idx in enumerate(covered):
            if j == 0:
                labels[idx] = "B-" + label
            else:
                labels[idx] = "I-" + label

    # Append tokens with tags
    for tok, lab in zip(tokens, labels):
        conll_lines.append(f"{tok} {lab}")
    conll_lines.append("")  # Sentence boundary

# Save to file
with open("dataset.conll", "w", encoding="utf-8") as f:
    f.write("\n".join(conll_lines))

print("✅ Exported to dataset.conll in CoNLL format")
