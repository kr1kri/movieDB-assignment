import psycopg2
from dataRetrieval import now_playing, gr_movies, crew_data, directors

conn = psycopg2.connect(
    database="greekmovies",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

for movie in now_playing:
    movie_id = movie['id']
    title = movie['title']
    description = movie['overview']
    original_title = movie['original_title']

    cur.execute(
        "INSERT INTO gr_movies (id, title, description, original_title) VALUES (%s, %s, %s, %s)",
        (movie_id, title, description, original_title)
    )

for movie in gr_movies:
    movie_id = movie['id']
    title = movie['title']
    description = movie['overview']
    original_title = movie['original_title']
    release_date = movie['release_date']
    imdb_id = movie['imdb_id']

    cur.execute(
        "INSERT INTO movies (id, title, description, original_title, release_date, imdb_id) VALUES (%s, %s, %s, %s, %s, %s)",
        (movie_id, title, description, original_title, release_date, imdb_id)
    )

for person in crew_data:
    crew_id = person['id']
    credit_id = person['credit_id']
    department = person['department']
    job = person['job']
    name = person['name']
    original_name = person['original_name']

    cur.execute(
        "INSERT INTO crew (crew_id, credit_id, department, job, name, original_name) VALUES (%s, %s, %s, %s, %s, %s)",
        (crew_id, credit_id, department, job, name, original_name)
    )

for director in directors:
    director_id = director['id']
    credit_id = director['credit_id']
    imdb_link = director['imdb_link']
    name = director['name']
    original_name = director['original_name']

    cur.execute(
        "INSERT INTO directors (director_id, credit_id, imdb_link, name, original_name) VALUES (%s, %s, %s, %s, %s)",
        (director_id, credit_id, imdb_link, name, original_name)
    )

conn.commit()
conn.close()
