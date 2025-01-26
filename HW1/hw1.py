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
    cursor = sqlite_connection.cursor()

    #CREATE TABLE QUERY
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        bookOrder INTEGER, 
        title TEXT,
        sandersonCoWrote BOOLEAN,
        goodreadsAverage FLOAT,
        mcburneyScore INTEGER,
        mcburneyReview TEXT)
        ''')

    #INSERT VALUES QUERY
    for book in books:
        values = []
        for col in ["order","title","sandersonCoWrote","goodreadsAverage","mcburneyScore","mcburneyReview"]:
            if col in book:
                values.append(book[col])
            else:
                values.append(None)
        cursor.execute("INSERT INTO Books (bookOrder, title, sandersonCoWrote, goodreadsAverage, mcburneyScore, mcburneyReview) VALUES(?,?,?,?,?,?)", tuple(values))

    sqlite_connection.commit()
    sqlite_connection.close()
    print('Completed reading json file to database.')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Correct Usage: python hw1.py <.json file> <.sqlite file>')
    else:
        main(sys.argv[1], sys.argv[2])