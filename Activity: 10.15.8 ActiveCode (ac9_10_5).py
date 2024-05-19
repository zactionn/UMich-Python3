fileref = open("school_prompt.txt","r")
three = []

for line in fileref:
    words = line.strip().split() #Split line into words and remove leading/trailing whitespaces
    if len(words) >=3:
        three.append(words[2])

print(three) 
fileref.close()

    
