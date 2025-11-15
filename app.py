
from utils import clean_text, count_frequency, sort_by_frequency_desc, export_frequencies_to_csv
from pathlib import Path


INPUT_FILE = Path("input.txt")


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    with open("input.txt", "r", encoding="utf-8") as file:
        content = file.read()

    clean_words = clean_text(content)
    counted_words=count_frequency(clean_words)
    sorted_words=sort_by_frequency_desc(counted_words)
    word_display(sorted_words)
    export_frequencies_to_csv(sorted_words)

def word_display(sorted_words):
    print("Top 10 most frequent words:")
    for word, count in sorted_words[:10]:
        print(word, count)

if __name__ == "__main__":
    main()
