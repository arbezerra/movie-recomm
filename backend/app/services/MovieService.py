from app import db


def paginate(page, limit):
    conn = db.get()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM movie ORDER BY popularity DESC OFFSET %s LIMIT %s;",
        ((page-1)*limit, limit)
    )
    movies = cur.fetchall()
    cur.close()

    return movies
