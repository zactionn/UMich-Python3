sally = "sally sells sea shells by the sea shore"

characters = {}

for c in sally:
    characters[c] = characters.get(c, 0) + 1
    
# Find the character with the maximum count
best_char = max(characters, key=characters.get)

print(characters)
print(f"The character that appears most often is '{best_char}'")

