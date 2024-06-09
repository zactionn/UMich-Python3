import requests_with_caching
import json

def get_movies_from_tastedive(movie_name):      
    dest_url = "https://tastedive.com/api/similar"
    dp = {'q': movie_name, 'type': 'movies', 'limit':5} #dictionary of parameters to be sent in the request
    resp = requests_with_caching.get(dest_url, params = dp)
    return resp.json()

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
print(get_movies_from_tastedive("Black Panther"))

