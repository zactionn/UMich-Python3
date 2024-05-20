def stop_at_four(numbers):
    newlist = []
    index = 0
    while index < len(numbers):
        if numbers[index] == 4:
            break
        newlist.append(numbers[index])
        index += 1
    return newlist