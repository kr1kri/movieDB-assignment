import os
import requests

api_key = os.getenv('API_KEY') #export API_KEY=<API_KEY>
params = {"api_key": api_key, "region": "GR"}
base_url = "https://api.themoviedb.org/3/"

now_playing_endpoint = base_url + "movie/now_playing"
response = requests.get(now_playing_endpoint, params=params)
now_playing = response.json()["results"]

directors = []

for movie in now_playing:
    credits_endpoint = base_url + f"movie/{movie['id']}/credits"
    credits_response = requests.get(credits_endpoint, params=params)
    crew_data = credits_response.json()["crew"]
    directors += [person for person in crew_data if person['job'] == "Director"]

for director in directors:
    person_endpoint = base_url + f"person/{director['id']}"
    person_response = requests.get(person_endpoint, params=params)
    imdb_id = person_response.json()['imdb_id']
    director['imdb_link'] = f"https://www.imdb.com/name/{imdb_id}"
