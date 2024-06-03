punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

string = ''
def strip_punctuation(word: str) -> str:
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word