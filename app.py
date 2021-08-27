from flask import Flask, redirect, render_template, request, flash, url_for, make_response
import models
import db_init


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():
    conn = models.db_connect()

    if request.method == 'POST':
        url = request.form['url']

        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))

        hashid = models.short_link_create(url)
        short_url = request.host_url + hashid

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')


@app.route('/stats')
def stats():
    conn = models.db_connect()
    contents = conn.execute('SELECT * FROM shorter;').fetchall()
    conn.close()
    stats = []

    for content in contents:
        corrected_date = '.'.join(x for x in content['created_at'].split()[0].split('-')[::-1])
        corrected_time = ':'.join(x for x in content['created_at'].split()[1].split(':')[:2])
        stats.append({
            'id': content[0],
            'long_url': content[1],
            'short_url': request.host_url + content[2],
            'created_at': corrected_time + ' ' + corrected_date,
            'redirects': content[4]
        })
    print(stats)
    return render_template('stats.html', stats=stats)


@app.route('/<string:link>/', methods=['GET'])
def go_on_link(link):
    conn = models.db_connect()
    cur = conn.cursor()
    cur.execute("SELECT long_url FROM shorter WHERE short_url = ?;", (link, ))
    res = cur.fetchone()
    if res:
        cur.execute("SELECT redirects FROM shorter WHERE short_url = ?;", (link, ))
        redir_count = int(cur.fetchone()[0]) + 1
        cur.execute(f"UPDATE shorter SET redirects = ? WHERE short_url = ?", (redir_count, link))
        conn.commit()
        conn.close()
        return redirect(res[0].replace(request.host_url, ''), code=302)
    else:
        return make_response(f"<h2>Не знайдено посилання!<hr>Спершу додайте його тут -> "
                             f"<a href='{request.host_url}'>{request.host_url}</a><br><br>Список доступних URL ->  "
                             f"<a href='{request.host_url}stats'>{request.host_url}stats</a></h2>")


if __name__ == '__main__':
    db_init.initialize_db()
    app.run(debug=False)