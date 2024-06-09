"2. Using filter, filter lst so that it only contains words containing the letter “o”. Assign to variable lst2. Do not hardcode this."

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = list(filter(lambda x: 'o' in x, lst))
print(lst2)
