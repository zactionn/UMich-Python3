import requests_with_caching
import json


# get movie title and return dictionary of information on movie
def get_movie_data(movie_name):      
    api_key = "eb4064d8"
    dest_url = "http://www.omdbapi.com/"
    dp = {'apikey': api_key, 't': movie_name, 'r': 'json'} #dictionary of parameters to be sent in the request
    resp = requests_with_caching.get(dest_url, params = dp)
    return resp.json()

