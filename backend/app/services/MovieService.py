from app import db


def get_all():
    conn = db.get()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            M.*, array_agg(DISTINCT G.genre_id) as genre
        FROM movie M JOIN movie_genre G ON G.movie_id=M.id
        GROUP BY M.id
        ORDER BY M.popularity DESC;"""
    )
    movies = cur.fetchall()
    cur.close()

    return movies


def get_map():
    conn = db.get()
    cur = conn.cursor()

    cur.execute("SELECT * FROM movie_map")
    map = cur.fetchall()
    cur.close()

    return map


def get_stared(user_id):
    conn = db.get()
    cur = conn.cursor()

    cur.execute("SELECT * FROM user_star_movie WHERE user_id=%s;", (user_id,))
    map = cur.fetchall()
    cur.close()

    return map


def get_by_ids(ids):
    conn = db.get()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT
            M.*, array_agg(DISTINCT G.genre_id) as genre
        FROM movie M JOIN movie_genre G ON G.movie_id=M.id
        WHERE id IN %s
        GROUP BY M.id;""",
        (ids,)
    )
    movies = cur.fetchall()
    cur.close()

    return movies


def paginate(page, limit):
    conn = db.get()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            M.*, array_agg(DISTINCT G.genre_id) as genre
        FROM movie M JOIN movie_genre G ON G.movie_id=M.id
        GROUP BY M.id
        ORDER BY RANDOM()
        OFFSET %s LIMIT %s;""",
        ((page-1)*limit, limit)
    )
    movies = cur.fetchall()
    cur.close()

    return movies
