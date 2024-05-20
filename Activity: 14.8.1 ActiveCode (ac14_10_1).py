


def sublist(x:list) -> list:
    index = 0
    sublist = []
    while index < len(x):
        if x[index] == 5:
            break
        sublist.append(x[index])
        index += 1
    return sublist
        