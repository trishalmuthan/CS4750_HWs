import json
import sqlite3
import sys

def main(json_file, sqlite_file):
    print(json_file)
    print(sqlite_file)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Correct Usage: python hw1.py <JSON file> <.sqlite DB file>')
    else:
        main(sys.argv[1], sys.argv[2])