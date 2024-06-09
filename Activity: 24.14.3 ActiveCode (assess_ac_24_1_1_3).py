import requests_with_caching
import json


def get_movies_from_tastedive(movie_name):      
    dest_url = "https://tastedive.com/api/similar"
    dp = {'q': movie_name, 'type': 'movies', 'limit':5} #dictionary of parameters to be sent in the request
    resp = requests_with_caching.get(dest_url, params = dp)
    return resp.json()



def extract_movie_titles(json_data):
    return [movie['Name'] for movie in json_data['Similar']['Results']] #extracting the movie names from the response by iterating over each item in the list of movies and extracting the name

#It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.


def get_related_titles(movie_titles):
    related_titles = set()
    for movie in movie_titles:
        json_data = get_movies_from_tastedive(movie)
        if json_data:
            related_movies = extract_movie_titles(json_data)
            related_titles.update(related_movies)

    return list(related_titles)