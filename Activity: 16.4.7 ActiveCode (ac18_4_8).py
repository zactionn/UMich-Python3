
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys = [key for key, value in sorted(dictionary.items(), key=lambda item: item[0])]

for key in sorted_keys:
    print(key)