s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0

for char in s:
        if char in vowels:
            num_vowels += 1

print(num_vowels)


