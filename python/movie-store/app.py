from sqlite3 import Timestamp
import database
import datetime

menu = """ Please select one of the following options:
1) Add new movies
2) View upcoming movies
3) View all movies
4) Watch a movie
5) View watched movies
6) Exit

Your selection: """

welcome = "Welcome to watchlist app!"

print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Which movies you want to store ?: ")
    release_date = input("When was this released in (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    print(timestamp)
    database.add_movie(title, timestamp)


def clean_table():
    promt_cleanup = input("Do you want to drop the table? Y/N : ")
    if promt_cleanup == "Y":
        database.drop_table()
    else:
        print("Okay don't worry we haven't dropped the table")


prompt_add_movie()
clean_table()
