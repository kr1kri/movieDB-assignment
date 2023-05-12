## Description

The purpose of this task was to create a script that will use the MovieDB API to retrieve and store movie information into a relational database.

## Instructions

1) Install the required packages
```
pip install -r requirements.txt
```

2) Create the database and the tables. For the purpose of the specific task, PostgreSQL database was used.
```
psql -U <username> -d <database> -a -f databaseCreation.sql
```

3) Retrieve data from the MovieDB API and store them into the database.
```
py fillDatabase.py
```

4) Execute the cli python file to retrieve the data regarding:
* the movies that are currently playing in the Greek theaters.
```
py cli.py --movies
```
* the directors of the movies that are currently playing in the Greek theaters.
```
py cli.py --directors
```
