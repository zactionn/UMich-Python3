
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# strip punctuation
def strip_punctuation(word: str) -> str:
    string = ''
    for char in punctuation_chars:
        word = word.replace(char, "")
    return word

def get_neg(text: str) -> int:
    text = text.lower()
    text_without_punctuation = strip_punctuation(text)
    words = text_without_punctuation.split()
    count_pos = 0
    for word in words:
        if word in negative_words:
            count_pos += 1
    return count_pos

#list of neg words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

