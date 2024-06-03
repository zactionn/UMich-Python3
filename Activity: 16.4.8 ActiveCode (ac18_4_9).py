groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

# Sort the dictionary by keys and store the sorted keys in a list
grocery_keys_sorted = [key for key, value in sorted(groceries.items(), key=lambda item: item[0])]

# Iterate over the sorted keys and print them
for key in grocery_keys_sorted:
    print(key)
