fileref = open("travel_plans.txt","r")
content = fileref.read() #read the entire file content into a string
num_begin_chars = 33 #initialize the variable outside the loop
first_chars = content[:num_begin_chars]
print(first_chars) 
fileref.close()

    
