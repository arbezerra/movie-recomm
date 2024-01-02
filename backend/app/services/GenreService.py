from app import db


def get_all():
    conn = db.get()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM genre;"
    )
    genres = cur.fetchall()
    cur.close()

    return genres

