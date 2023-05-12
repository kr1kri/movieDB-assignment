CREATE DATABASE greekmovies
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    original_title TEXT NOT NULL,
    country_playing TEXT
);

CREATE TABLE crew (
    crew_id INTEGER PRIMARY KEY,
    credit_id TEXT NOT NULL,
    department TEXT NOT NULL,
    job TEXT NOT NULL,
    name TEXT NOT NULL,
    original_name TEXT NOT NULL
);

CREATE TABLE directors (
    director_id INTEGER PRIMARY KEY,
    credit_id TEXT NOT NULL,
    imdb_link TEXT,
    name TEXT NOT NULL,
    original_name TEXT NOT NULL
);
