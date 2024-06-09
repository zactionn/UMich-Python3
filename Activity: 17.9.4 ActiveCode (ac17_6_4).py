
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.

if 'data' in nested:
    data = True
else:
    data = False

# Check if 24 is in the nested list under the key 'data'

if 24 in nested['data']:
    twentyfour = True
else:
    twentyfour = False


# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.

if 'whole' not in nested['window']:
    whole = True
else:
    whole = False


# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.

if 'physics' in nested:
    physics = True
else:
    physics = False