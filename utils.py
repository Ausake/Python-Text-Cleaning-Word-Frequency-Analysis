import string


#convert to lowercase, suppress punctuation,

def clean_text(text: str) -> list[str]:
    text = text_to_lowercase(text)
    text = text_suppress_punctuation(text)
    textlist = text_to_list(text)
    return textlist

def count_frequency(words: list[str]) -> dict[str, int] :
    words_frequency = {}
    for word in words:
        if word not in words_frequency:
            words_frequency[word] = 1
        else:
            words_frequency[word] += 1
    return words_frequency


def text_to_lowercase(text: str) -> str:
    return text.lower()

def text_suppress_punctuation(text: str) -> str :
    return text.translate(str.maketrans('', '', string.punctuation))


def text_to_list(text: str) -> list[str] :
    return text.split()

def sort_by_frequency_desc(words: dict[str,int]) -> list[tuple[str,int]] :

    return sorted(words.items(), key=lambda x:x[1], reverse=True)

def export_frequencies_to_csv(text_sorted: list[tuple[str, int]]) -> None:
    with open('output.csv', 'w', encoding="utf-8") as output_file:
        output_file.write("word,count\n")
        for word,count in text_sorted:
            output_file.write(f"{word},{count}\n")
