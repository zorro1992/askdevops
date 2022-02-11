from multiprocessing import connection


import sqlite3
from tkinter import INSERT

CREATE_MOVIES_TABLE = """ CREATE TABLE IF NOT EXISTS movies(
    title TEST,
    release_timestamp REAL,
    watched INTEGER
)
"""

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?,?,0);"
DROP_MOVIES = "DROP TABLE IF EXISTS movies"

connection = sqlite3.connect("movies.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def drop_table():
    with connection:
        connection.execute(DROP_MOVIES)
    print("Table is dropped")
