
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

def second_let(strg: str) -> str:
    return strg[1] if len(strg) > 1 else ''
    
sorted_by_second_let =sorted(ex_lst, key=second_let)
print(sorted_by_second_let)    

