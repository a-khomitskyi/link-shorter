import sqlite3
from os import path


def initialize_db():
    if not path.exists('database.sqlite3'):
        with open('database.sqlite3', 'w') as f:
            pass
        conn = sqlite3.connect('database.sqlite3')
        cur = conn.cursor()
        cur.executescript(
           """CREATE TABLE shorter (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                long_url TEXT NOT NULL UNIQUE,
                short_url VARCHAR (50) UNIQUE NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                redirects INTEGER NOT NULL DEFAULT 0
                );""")
        conn.commit()
        conn.close()
        print('Created DB!')
    else:
        print('Operation aborted. DB exists!')


if __name__ == '__main__':
    initialize_db()