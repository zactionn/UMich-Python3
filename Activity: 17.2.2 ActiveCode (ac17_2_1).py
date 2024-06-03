"Extract the value associated with the key color and assign it to the variable color. Do not hard code this."

info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }
def extract_value(key):
    for key, value in info.items(): # for each key and its value
        if key == 'personal_data': # if the key is personal data
            for key2, value2 in value.items(): # for each key and its value
                if key2 == 'physical_features': # if the key is physical features
                    return value2['color'] # return the value of color
        

color = extract_value('color')

