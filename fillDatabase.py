import os
import psycopg2
from dataRetrieval import now_playing, crew_data, directors

db_user = os.getenv('POSTGRES_UNAME')
db_pwd = os.getenv('POSTGRES_PWD')

conn = psycopg2.connect(
    database="greekmovies",
    user=db_user,
    password=db_pwd,
    host="localhost",
    port="5432"
)
cur = conn.cursor()
conn.autocommit = True

movies_data = [(movie['id'], movie['title'], movie['overview'], movie['original_title'], 'GR') for movie in now_playing]
movies_query = "INSERT INTO movies (id, title, description, original_title, country_playing) VALUES (%s, %s, %s, %s, %s) " \
               "ON CONFLICT (id) DO UPDATE SET (title, description, original_title, country_playing) = " \
               "(EXCLUDED.title, EXCLUDED.description, EXCLUDED.original_title, EXCLUDED.country_playing)"
cur.executemany(movies_query, movies_data)

person_data = [(person['id'], person['credit_id'], person['department'], person['job'], person['name'], person['original_name']) for person in crew_data]
crew_query = "INSERT INTO crew (crew_id, credit_id, department, job, name, original_name) VALUES (%s, %s, %s, %s, %s, %s) " \
             "ON CONFLICT (crew_id) DO UPDATE SET (credit_id, department, job, name, original_name) = " \
             "(EXCLUDED.credit_id, EXCLUDED.department, EXCLUDED.job, EXCLUDED.name, EXCLUDED.original_name)"
cur.executemany(crew_query, person_data)

directors_data = [(director['id'], director['credit_id'], director['imdb_link'], director['name'], director['original_name']) for director in directors]
directors_query = "INSERT INTO directors (director_id, credit_id, imdb_link, name, original_name) VALUES (%s, %s, %s, %s, %s) " \
                  "ON CONFLICT (director_id) DO UPDATE SET (credit_id, imdb_link, name, original_name) = " \
                  "(EXCLUDED.credit_id, EXCLUDED.imdb_link, EXCLUDED.name, EXCLUDED.original_name)"
cur.executemany(directors_query, directors_data)

conn.commit()
conn.close()
