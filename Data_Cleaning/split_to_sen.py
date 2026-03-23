import re

def clean_and_split(text):
    # Remove verse references like 1:2, 2:10
    text = re.sub(r'\d+:\d+', '', text)

    # Remove standalone numbers (verse numbers)
    text = re.sub(r'\b\d+\b', '', text)

    # Normalize spaces
    text = re.sub(r'\s+', ' ', text)

    # Split sentences
    sentences = re.split(r'[.!?]', text)

    # Clean sentences
    sentences = [s.strip() for s in sentences if len(s.strip()) > 2]

    return sentences


with open("ActsandLuke.txt", "r", encoding="utf-8") as f:
    text = f.read()

sentences = clean_and_split(text)

with open("sentences_clean.txt", "w", encoding="utf-8") as f:
    for s in sentences:
        f.write(s + "\n")

print(f"Total cleaned sentences: {len(sentences)}")