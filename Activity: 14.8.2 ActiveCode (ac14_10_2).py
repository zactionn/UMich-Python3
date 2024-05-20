


def check_nums(x:list) -> list:
    index = 0
    sublist = []
    while index < len(x):
        if x[index] == 7:
            break
        sublist.append(x[index])
        index += 1
    return sublist
        