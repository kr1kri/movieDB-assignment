CREATE TABLE gr_movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    original_title TEXT NOT NULL
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    original_title TEXT NOT NULL,
    release_date DATE,
    imdb_id TEXT
);

CREATE TABLE crew (
    crew_id INTEGER NOT NULL,
    credit_id TEXT PRIMARY KEY,
    department TEXT NOT NULL,
    job TEXT NOT NULL,
    name TEXT NOT NULL,
    original_name TEXT NOT NULL
);

CREATE TABLE directors (
    director_id INTEGER NOT NULL,
    credit_id TEXT PRIMARY KEY,
    imdb_link TEXT,
    name TEXT NOT NULL,
    original_name TEXT NOT NULL
);