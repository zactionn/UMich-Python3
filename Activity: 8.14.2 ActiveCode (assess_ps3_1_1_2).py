

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

words = sentence.split(' ')
same_letter_count = 0
charcount = 0

for n in words:
   charcount = len(n)
   if n[0] == n[-1]:
       same_letter_count +=  1  
       print(n)
    



