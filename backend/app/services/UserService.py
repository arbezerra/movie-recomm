from app import db
import traceback


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


def insert(user):
    try:
        conn = db.get()
        cur = conn.cursor()

        cur.execute(
            """INSERT INTO users (name, email, password)
            VALUES (%s,%s,%s) RETURNING id;""",
            (user['name'], user['email'], user['password'])
        )
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()

        user['id'] = user_id

        return user
    except Exception:
        print(traceback.format_exc())
        return False
