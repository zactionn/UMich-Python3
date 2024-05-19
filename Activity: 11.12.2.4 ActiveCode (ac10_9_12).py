freq_words = {}

for word in str1.split():
    freq_words[word] = freq_words.get(word, 0) + 1

print(freq_words)