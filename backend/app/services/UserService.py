from app import db


def by_email(email):
    conn = db.get()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=%s;",
        (email,)
    )
    user = cur.fetchone()
    cur.close()

    return user
