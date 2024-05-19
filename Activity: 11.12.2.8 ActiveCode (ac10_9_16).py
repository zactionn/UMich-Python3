string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
lowercase_string = string1.lower()
letter_counts = {}

for c in lowercase_string:
    letter_counts[c] = letter_counts.get(c, 0) + 1
    
