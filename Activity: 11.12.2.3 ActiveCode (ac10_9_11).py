s1 = "hello"

counts = {}
char_count = 0


for char in s1: 
    counts[char] = counts.get(char,0) + 1
        
print(counts) 
