lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

def double_element(element):
    if isinstance(element, list):
        return element + element
    elif isinstance(element, str):
        return element + element
    elif isinstance(element, int):
        return element * 2
    else:
        return "I don't know what to do with this"

greeting_doubled = list(map(double_element, lst))


print(greeting_doubled)