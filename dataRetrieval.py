import requests
from pprint import pprint

# Define API endpoint and parameters
endpoint = "https://api.themoviedb.org/3/movie/now_playing"
params = {"api_key": "bbb0e77b94b09193e6f32d5fac7a3b9c", "region": "GR"}

# Make API request and get movie data
response = requests.get(endpoint, params=params)
now_playing = response.json()["results"]

# Collect information for each movie
gr_movies = []
directors = []

for movie in now_playing:
    # Get movie details
    movie_endpoint = f"https://api.themoviedb.org/3/movie/{movie['id']}"
    movie_response = requests.get(movie_endpoint, params=params)
    gr_movies.append(movie_response.json())

    # Get movie credits and extract directors
    credits_endpoint = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits"
    credits_response = requests.get(credits_endpoint, params=params)
    crew_data = credits_response.json()["crew"]
    directors += [person for person in crew_data if person['job'] == "Director"]

# Get IMDb IDs for directors
for director in directors:
    person_endpoint = f"https://api.themoviedb.org/3/person/{director['id']}"
    person_response = requests.get(person_endpoint, params=params)
    imdb_id = person_response.json()['imdb_id']
    director['imdb_link'] = f"https://www.imdb.com/name/{imdb_id}"

# pprint(now_playing[0])
# pprint(gr_movies[0])
# pprint(crew_data[0])
# pprint(directors[0])

