str1 = "peter piper picked a peck of pickled peppers"
freq ={} #empty dictionary
char_count = 0 #initialize the accumulator variable
char = ''

for char in str1: 
    freq[char] = freq.get(char,0) + 1
        
print(freq) 
    
