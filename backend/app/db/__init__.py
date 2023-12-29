from flask import g
import psycopg2
from app import config


def init_app(app):
    app.teardown_appcontext(close)


def get():
    if 'db' not in g:
        g.db = connect()
    return g.db


def close():
    db = g.pop('db', None)
    if db is not None:
        db.close()


def connect():
    conn = psycopg2.connect(
        host=config.DB_HOST,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASS,
    )
    return conn
