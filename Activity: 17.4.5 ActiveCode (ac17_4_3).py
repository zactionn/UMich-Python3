"3. Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings."


L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]


def search_b_strings(L):
    b_strings = []
    for item in L:
        for subitem in item:
            if 'b' in subitem.lower():
                b_strings.append(subitem)
    return b_strings

b_strings = search_b_strings(L)
