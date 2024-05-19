sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

wrd_d = {}

for word in sent.split():
    wrd_d[word] = wrd_d.get(word, 0) + 1

print(wrd_d)

