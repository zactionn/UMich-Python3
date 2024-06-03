punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# strip punctuation
def strip_punctuation(word: str) -> str:
    string = ''
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word

def get_pos(text: str) -> int:
    text = text.lower()
    text_without_punctuation = strip_punctuation(text)
    words = text_without_punctuation.split()
    count_pos = 0
    for word in words:
        if word in positive_words:
            count_pos += 1
    return count_pos

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())