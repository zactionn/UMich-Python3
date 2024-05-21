def test(reqint: int, opbool: bool = True, dict1: dict = {2: 3, 4: 5, 6: 8}) -> int:
    if opbool: 
        if reqint in dict1:
            return dict1[reqint]
        else :
            return None
    else:
        return False