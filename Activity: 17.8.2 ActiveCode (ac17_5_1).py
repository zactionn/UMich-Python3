"Iterate through the list so that if the character ‘m’ is in the string, then it should be added to a new list called m_list. Hint: Because this isn’t just a list of lists, think about what type of object you want your data to be stored in. Conditionals may help you."


def search_for_m(data):
    m_list = []
    
    def recursive_search(string):
        for item in string:
            if isinstance(item, list):
                recursive_search(item)
            elif item =='m':
                m_list.append(item)
    recursive_search(string)
    return m_list

m_list = search_for_m(d)
