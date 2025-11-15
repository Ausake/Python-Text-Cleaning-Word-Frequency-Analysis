# Word Frequency Analyzer

A small text-processing project that:
- cleans raw text (lowercasing, punctuation remove),
- splits it into words,
- counts word frequencies,
- sorts results by frequency,
- and exports them to a CSV file.

## How it works

The project is split into two files:

- `utils.py`
  Contains helper functions:
  - `clean_text(text: str) -> list[str]`
  - `count_frequency(words: list[str]) -> dict[str, int]`
  - `sort_by_frequency_desc(freq: dict[str, int]) -> list[tuple[str, int]]`
  - `export_all(sorted_words) -> None`

  - `app.py`
  Orchestrates the workflow:
  1. Reads `input.txt`
  2. Cleans the text
  3. Counts word frequencies
  4. Sorts them in descending order
  5. Prints the top 10 words
  6. Exports all results to `output.csv`

## How to run

```bash
python app.py