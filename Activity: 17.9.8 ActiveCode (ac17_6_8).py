"Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third."

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = [sublist[2] for sublist in l_of_l]
print(third)
