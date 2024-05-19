org = "your original string here"  # Replace this with your original string
stopwords = ["to", "a", "for", "by", "an", "am", "the", "with", "in", "and", "of"]  # Add or remove stopwords as needed

# Split the original string into words
words = org.split()

# Create the acronym
acro = ''.join(word[0].upper() for word in words if word not in stopwords)

print(acro)
