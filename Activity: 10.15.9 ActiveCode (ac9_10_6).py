
fileref = open("emotion_words.txt","r")
emotions = []

for line in fileref:
    words = line.strip().split() #Split line into words and remove leading/trailing whitespaces
    if len(words) >=1:
        emotions.append(words[0])

print(emotions) 
fileref.close()