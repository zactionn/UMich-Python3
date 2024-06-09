"2. Below, we have provided a list of lists that contain information about people. Write code to create a new list that contains every person’s last name, and save that list as last_names."

info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

def return_lastnames(info): # function to return a list of last names from a list
    last_names = [] # empty list to append to
    for person in info: 
        last_names.append(person[1]) # add each last name to the new list named last_names
    return last_names
print(return_lastnames(info))
        
last_names = return_lastnames(info)

