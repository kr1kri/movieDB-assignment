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
