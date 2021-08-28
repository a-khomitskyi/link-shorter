import sqlite3
from hashids import Hashids
import re


def db_connect():
    conn = sqlite3.connect('database.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def is_valid_url(url):
    if 'https://' not in url or 'http://' not in url:
        url = 'https://' + url
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    p = re.compile(regex)

    if url is None:
        return False

    return True if re.search(p, url) else False


def short_link_create(link):
    if 'https://' not in link or 'http://' not in link:
        link = 'https://' + link

    hashids = Hashids(salt=f'{link}')
    hashid = hashids.encode(123)  # 'nVB'
    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO shorter (long_url, short_url) VALUES (?, ?)", (link, hashid))
        conn.commit()
        conn.close()
    except Exception as ex:
        print(ex)
    return hashid


if __name__ == '__main__':
    # print(short_link_create('https://google.com/'))
    print(is_valid_url('https://google.com/'))
    print(is_valid_url('https://fasfasfasf'))
    print(is_valid_url('https://аіппіпіпіа.com'))
    print(is_valid_url('https://google.ua/'))
    print(is_valid_url('google.com'))