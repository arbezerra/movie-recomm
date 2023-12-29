from app import db


def get_all():
    conn = db.get()
    cur = conn.cursor()

    cur.execute("SELECT * FROM movie")
    movies = cur.fetchall()
    cur.close()

    return movies
