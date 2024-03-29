import os
from dotenv import load_dotenv
load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
TMDB_TOKEN = os.getenv("TMDB_TOKEN")
DEBUG = os.getenv("DEBUG") or False

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# RabbitMQ
Q_HOST = os.getenv("Q_HOST")
