
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
sent = "The water earth and air are vital"

split_org = sent.split()

#remove stopwords

new_org = [word for word in split_org if word.lower() not in stopwords]
new_org = [word.upper() for word in new_org]

first_letters = [word[:2] for word in new_org if word]

acro = '. '.join(first_letters) 


    
     
