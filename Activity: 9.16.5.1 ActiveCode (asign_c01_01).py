scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

sort_scores = scores.split(' ')

int_scores = [int(item) for item in sort_scores]
print(sort_scores)

more_than_90 = 0

for n in int_scores:
    if n > 89:
        more_than_90 += 1
        
a_scores = more_than_90

print(a_scores)