
fileref = open("school_prompt.txt","r")
p_words = []
char = "p"

for line in fileref:
    words = line.strip().split() #Split line into words and remove leading/trailing whitespaces
    for word in words:
        if char in word:
            p_words.append(word)

print(p_words) 
fileref.close()

    
