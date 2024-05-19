sally = "sally sells sea shells by the sea shore and by the road"

characters = {}

for c in sally:
    characters[c] = characters.get(c, 0) + 1
    

# Find the character with the minimum count
worst_char = min(characters, key=characters.get)

print(characters)
print(f"The character that appears the least is '{worst_char}'")