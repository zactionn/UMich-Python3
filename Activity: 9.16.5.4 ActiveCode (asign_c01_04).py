p_phrase = "was it a car or a cat I saw"

# Reverse the phrase by character
r_phrase = p_phrase[::-1]

# Check if the original phrase, ignoring case and spaces, is a palindrome
if r_phrase.lower().replace(" ", "") != p_phrase.lower().replace(" ", ""):
    print("not a palindrome")
else:
    print("is a palindrome")
