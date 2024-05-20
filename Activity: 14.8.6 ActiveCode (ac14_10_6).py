def beginning(x:list) -> list:
    index = 0 #initialize the index
    thelist = [] #initialize the list, no a good idea to name the sublist as the same as the function
    while index < len(x) and len(thelist) <10: #while the index is incrementally accumulated until it is less than the length of the list
        if x[index] == "bye":
            break
        thelist.append(x[index])
        index += 1
    return thelist
        