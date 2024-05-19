p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

low_d = {}

for char in p:
    char = char.lower()  # Convert the character to lowercase
    if char in low_d:
        low_d[char] += 1
    else:
        low_d[char] = 1
        


print(low_d)
