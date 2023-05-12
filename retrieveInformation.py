import psycopg2
import os
import argparse

parser = argparse.ArgumentParser(description='Choose the database information you want to retrieve')
parser.add_argument('--movies', action='store_true', help='Select movies')
parser.add_argument('--directors', action='store_true', help='Select directors')
args = parser.parse_args()

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

if args.movies:
    cur.execute("SELECT title, description, original_title FROM movies")
    data = cur.fetchall()
elif args.directors:
    cur.execute("SELECT name, imdb_link FROM directors")
    data = cur.fetchall()
else:
    print("Please specify the data you want to retrieve using --movies or --directors arguments")
    exit(1)

columns = [desc[0] for desc in cur.description]

print("|".join(columns))
for row in data:
    print("|".join(str(val) for val in row))

conn.close()
