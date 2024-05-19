items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

target = 'w'
wordlist = []

for item in items:
    if target in item:
        wordlist.append(item)
        
print(wordlist)
acc_num = len(wordlist)
