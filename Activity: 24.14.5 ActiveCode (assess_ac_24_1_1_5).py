"""Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0."""


# get movie title and return dictionary of information on movie
def get_movie_data(movie_name):      
    api_key = "eb4064d8"
    dest_url = "http://www.omdbapi.com/"
    dp = {'apikey': api_key, 't': movie_name, 'r': 'json'} #dictionary of parameters to be sent in the request
    resp = requests_with_caching.get(dest_url, params = dp)
    return resp.json()

# get movie rating from OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer

def get_movie_rating(result):
    if "Ratings" in result: 
        for rating in result['Ratings']: #loop through outer most list of dictionaries in the dictionary 
            if rating['Source'] == "Rotten Tomatoes": #loop through innermost list of dictionaries in the dictionary
                return int(rating['Value'].rstrip('%'))
        return 0