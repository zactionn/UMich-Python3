fileref = open("school_prompt.txt","r")
content = fileref.readlines() #read the entire file content into a list

num_lines = len(content)
print(num_lines) 
fileref.close()

    
