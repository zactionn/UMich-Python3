


def stop_at_z(x:list) -> list:
    index = 0 #initialize the index
    thelist = [] #initialize the list, no a good idea to name the sublist as the same as the function
    while index < len(x): #while the index is incrementally accumulated until it is less than the length of the list
        if x[index] == "z":
            break
        thelist.append(x[index])
        index += 1
    return thelist
        