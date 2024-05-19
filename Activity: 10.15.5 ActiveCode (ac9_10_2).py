fileref = open("emotion_words.txt","r")
content = fileref.read() #read the entire file content into a string
words = content.split() #split the content variable that holds the strings
num_words = len(words)
print(num_words) 
fileref.close()

    
