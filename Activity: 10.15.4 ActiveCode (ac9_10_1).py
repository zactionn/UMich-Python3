fileref = open("travel_plans.txt","r")
content = fileref.read() #read the entire file content into a string
num = len(content)
print(num) 
fileref.close()

    
