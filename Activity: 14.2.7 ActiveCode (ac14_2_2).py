
def stop_at_four(x: int) -> int:
    newlist = []
    index = 0
    while index < len(x):
        if x[index] == 4:
            break
        newlist.append(x[index])
        index += 1
    return newlist
        