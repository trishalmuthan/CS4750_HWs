import json
import sqlite3
import sys

def main(json_file, sqlite_file):
    print('Reading json file to database.')

    with open(json_file) as f:
        data = json.load(f)
    
    try:
        books = data['books']
    except KeyError:
        print('There is no books key in the given json file.')
        print('Database was not created.')
        return

    sqlite_connection = sqlite3.connect(sqlite_file)
    sqlite_cursor = sqlite_connection.cursor()

    #CREATE TABLE QUERY


    #INSERT VALUES QUERY


    sqlite_connection.close()
    print('Completed reading json file to database.')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Correct Usage: python hw1.py <.json file> <.sqlite file>')
    else:
        main(sys.argv[1], sys.argv[2])