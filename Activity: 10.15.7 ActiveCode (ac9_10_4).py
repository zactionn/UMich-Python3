fileref = open("school_prompt.txt","r")
content = fileref.read() #read the entire file content into a string
num_begin_chars = 30 #initialize the variable outside the loop
beginning_chars = content[:num_begin_chars]
print(beginning_chars) 
fileref.close()

    
