
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]

def find_item(a_list, value):
    for index, item in enumerate(a_list):
        if item == value:
            return [index]
        elif isinstance(item, list):
            result = find_item(item, value)
            if result is not None:
                return [index] + result
    return None

def get_nested_item(a_list, indices):
    for index in indices:
        a_list = a_list[index]
    return a_list

position = find_item(data, 'willow')
plant = get_nested_item(data, position)
