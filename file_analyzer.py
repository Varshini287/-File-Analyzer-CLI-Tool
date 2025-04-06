import sys
import string
from collections import Counter

# Define common English stop words
STOP_WORDS = {"the", "is", "and", "a", "an", "in", "on", "of", "to", "with", "that", "this", "it", "for", "as", "are"}

def clean_text(text):
    # Remove punctuation and make all words lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.lower()

def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        cleaned_text = clean_text(text)
        words = cleaned_text.split()
        filtered_words = [word for word in words if word not in STOP_WORDS]

        total_words = len(words)
        average_word_length = sum(len(word) for word in words) / total_words if total_words else 0

        word_frequencies = Counter(filtered_words)
        top_5_words = word_frequencies.most_common(5)

        # Sentence count by splitting at . ? !
        sentences = [s for s in text.replace('\n', ' ').split('.') if s.strip()]
        sentences += [s for s in text.split('?') if '?' in text]
        sentences += [s for s in text.split('!') if '!' in text]
        sentence_count = len(sentences)

        # Output results
        print("📄 File Analysis Report")
        print("---------------------------")
        print(f"Total words: {total_words}")
        print(f"Top 5 frequent words: {top_5_words}")
        print(f"Average word length: {average_word_length:.2f}")
        print(f"Number of sentences: {sentence_count}")

    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_analyzer.py <file_path>")
    else:
        analyze_file(sys.argv[1])
