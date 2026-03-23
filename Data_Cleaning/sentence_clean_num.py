import re

def remove_leading_numbers(sentences):
    cleaned = []

    for s in sentences:
        # Remove numbers attached to words at the beginning of tokens
        # Example: 38Ngə → Ngə
        s = re.sub(r'\b\d+([A-Za-zƏəƁɓƊɗƳƴ]+)', r'\1', s)

        # Also remove any remaining standalone numbers
        s = re.sub(r'\b\d+\b', '', s)

        # Normalize spaces
        s = re.sub(r'\s+', ' ', s).strip()

        if len(s.split()) > 3:
            cleaned.append(s)

    return cleaned


# Load your file
with open("sentences_final.txt", "r", encoding="utf-8") as f:
    sentences = f.readlines()

cleaned_sentences = remove_leading_numbers(sentences)

# Save output
with open("sentences_no_numbers.txt", "w", encoding="utf-8") as f:
    for s in cleaned_sentences:
        f.write(s + "\n")

print(f"Total sentences after removing numbers: {len(cleaned_sentences)}")