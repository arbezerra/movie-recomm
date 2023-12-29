import bcrypt
import psycopg2
import random
from app import config
from app.api.tmdb import API

api = API()

conn = psycopg2.connect(
    host=config.DB_HOST,
    database=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASS,
)

cur = conn.cursor()

cur.execute(
    "select exists(select * from information_schema.tables where table_name=%s)",
    ('genre',)
)

if cur.fetchone()[0]:
    print("db exists, skipping init")
else:
    cur.execute("""
    CREATE TABLE genre (
       id SERIAL PRIMARY KEY,
       name VARCHAR(255) NOT NULL
    );""")

    cur.execute("""
    CREATE TABLE movie (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        original_title VARCHAR(255) NOT NULL,
        overview TEXT NOT NULL,
        release_date DATE NOT NULL,
        popularity NUMERIC(10,3) NOT NULL,
        vote_average NUMERIC(2,1) NOT NULL,
        vote_count BIGINT NOT NULL,
        backdrop_path VARCHAR(255) NOT NULL,
        poster_path VARCHAR(255) NOT NULL
    );""")

    cur.execute("""
    CREATE TABLE movie_genre (
        movie_id INTEGER REFERENCES movie(id),
        genre_id INTEGER REFERENCES genre(id),
        CONSTRAINT movie_genre_key PRIMARY KEY (movie_id, genre_id)
    );""")

    cur.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    );""")

    cur.execute("""
    CREATE TABLE user_star_movie (
        user_id INTEGER REFERENCES users(id),
        movie_id INTEGER REFERENCES movie(id),
        stars INTEGER NOT NULL,
        CONSTRAINT user_star_movie_key PRIMARY KEY (user_id, movie_id)
    );""")

    genres = api.get(
        "/genre/movie/list?language=pt-BR",
    )['genres']

    cur.execute(
        "INSERT INTO genre (id, name) VALUES " +
        ','.join(cur.mogrify(
            "(%s,%s)", (genre['id'], genre['name'])).decode('utf8')
            for genre in genres)
    )
    movie_genres = []
    movies_ids = []

    for page in range(1, 11):
        movies = api.get(
            f"/movie/top_rated?language=pt-BR&page={page}&region=BR"
        )['results']
        cur.execute(
            "INSERT INTO movie VALUES " +
            ','.join(cur.mogrify(
                "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    m['id'],
                    m['title'],
                    m['original_title'],
                    m['overview'],
                    m['release_date'],
                    m['popularity'],
                    m['vote_average'],
                    m['vote_count'],
                    m['backdrop_path'],
                    m['poster_path'],
                )).decode('utf8') for m in movies
            )
        )
        for m in movies:
            movies_ids.append(m['id'])
            for g in m['genre_ids']:
                movie_genres.append((m['id'], g))

    cur.execute(
        "INSERT INTO movie_genre (movie_id, genre_id) VALUES " +
        ','.join(cur.mogrify(
            "(%s,%s)", mg).decode('utf8')
            for mg in movie_genres)
    )

    cur.execute(
        "INSERT INTO users (name, email, password) VALUES " +
        ','.join(cur.mogrify(
            "(%s,%s,%s)", (
                f"User {i}",
                f"user{i}@example.com",
                bcrypt.hashpw("123".encode('utf-8'), bcrypt.gensalt()),
            )).decode('utf8')
            for i in range(1, 11))
    )

    user_stars = []
    for user in range(1, 11):
        for movie in random.sample(movies_ids, 10):
            stars = random.randint(1, 5)
            user_stars.append((user, movie, stars))

    cur.execute(
        "INSERT INTO user_star_movie (user_id, movie_id, stars) VALUES " +
        ','.join(cur.mogrify(
            "(%s,%s,%s)", us).decode('utf8')
            for us in user_stars)
    )

    conn.commit()

    cur.close()
    conn.close()

    print("DB inited")
