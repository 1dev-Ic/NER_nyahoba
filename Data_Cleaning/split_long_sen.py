def split_to_18_words(sentences, max_len=18):
    new_sentences = []

    for s in sentences:
        words = s.split()

        # If sentence is short, keep it
        if len(words) <= max_len:
            new_sentences.append(s)
        else:
            # Split into chunks of max_len words
            for i in range(0, len(words), max_len):
                chunk = " ".join(words[i:i+max_len])
                if len(chunk.split()) >= 4:  # avoid very short fragments
                    new_sentences.append(chunk)

    return new_sentences


# Load your cleaned file
with open("sentences_no_numbers.txt", "r", encoding="utf-8") as f:
    sentences = [line.strip() for line in f if line.strip()]

# Apply splitting
final_sentences = split_to_18_words(sentences)

# Save result
with open("sentences_18words.txt", "w", encoding="utf-8") as f:
    for s in final_sentences:
        f.write(s + "\n")

print(f"Total sentences after splitting: {len(final_sentences)}")