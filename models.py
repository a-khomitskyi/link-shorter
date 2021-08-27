import sqlite3
from hashids import Hashids


def db_connect():
    conn = sqlite3.connect('database.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def short_link_create(link):
    if 'https://' not in link:
        link = 'https://' + link
    hashids = Hashids(salt=f'{link}')
    hashid = hashids.encode(123)  # 'nVB'
    conn = db_connect()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO shorter (long_url, short_url) VALUES (?, ?)", (link, hashid))
        conn.commit()
    except Exception as ex:
        print(ex)
    conn.close()
    return hashid


if __name__ == '__main__':
    print(short_link_create('https://google.com/'))
