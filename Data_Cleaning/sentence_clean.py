import re

def advanced_clean(sentences):
    cleaned = []

    for s in sentences:
        # Remove verse numbers like 33A, 34Na
        s = re.sub(r'^\d+[A-Za-z]*', '', s)

        # Remove standalone numbers
        s = re.sub(r'\b\d+\b', '', s)

        # Remove "Changhabal" headers
        s = re.sub(r'"?Changhabal.*?"?:?', '', s)

        # Remove copyright text
        s = re.sub(r'©.*', '', s)

        # Remove strange quotes
        s = re.sub(r'[“”‘’"]', '', s)

        # Normalize spaces
        s = re.sub(r'\s+', ' ', s).strip()

        # Remove very short/noisy lines
        if len(s.split()) > 3:
            cleaned.append(s)

    return cleaned


# Load sentences
with open("sentences_clean.txt", "r", encoding="utf-8") as f:
    sentences = f.readlines()

cleaned_sentences = advanced_clean(sentences)

# Save cleaned version
with open("sentences_final.txt", "w", encoding="utf-8") as f:
    for s in cleaned_sentences:
        f.write(s + "\n")

print(f"Final cleaned sentences: {len(cleaned_sentences)}")