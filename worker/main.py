import pika
import traceback
import os
import psycopg2
from psycopg2.extras import DictCursor
import pandas as pd
import umap
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")

db = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    cursor_factory=DictCursor,
)


def get_data():
    return pd.read_sql_query(
        """
        SELECT
            M.*, array_agg(DISTINCT G.genre_id) as genre
        FROM movie M JOIN movie_genre G ON G.movie_id=M.id
        GROUP BY M.id
        ORDER BY M.popularity DESC;""",
        f'postgresql+psycopg2://{user}:{password}@{host}/{database}'
    )


def tfidf(text):
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(text)
    return pd.DataFrame(
        x.toarray(),
        columns=vectorizer.get_feature_names_out()
    )


def one_hot(values):
    encoder = MultiLabelBinarizer()
    x = encoder.fit_transform(values)
    return pd.DataFrame(x, columns=encoder.classes_)


def process_data(data):
    processed = data[[
        'popularity',
        'vote_average',
        'vote_count',
    ]]
    processed['release_date'] = data['release_date'].apply(
        lambda x:  x.toordinal())
    processed = pd.concat(
        [processed, one_hot(data['genre'])], axis=1
    )
    processed = pd.concat(
        [processed, tfidf(data['title']+' '+data['overview'])], axis=1)
    return processed


def insert_result(data):
    cur = db.cursor()
    for index, row in data.iterrows():
        cur.execute("""
            INSERT INTO movie_map (id,x,y) VALUES (%s,%s,%s)
            ON CONFLICT (id)
            DO
                UPDATE SET x = EXCLUDED.x, y = EXCLUDED.y;
        """, (row['id'], row['x'], row['y'])
        )
    db.commit()


def work(ch, method, properties, body):
    print(f"START {body}")
    data = get_data()
    processed = process_data(data)
    result = umap.UMAP().fit_transform(processed.values)
    data['x'] = result[:, 0]
    data['y'] = result[:, 1]
    insert_result(data)
    print(f"DONE {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    print("Connecting to queue")
    conn = pika.BlockingConnection(
        pika.ConnectionParameters(host=os.getenv('Q_HOST'))
    )
    ch = conn.channel()
    ch.queue_declare(queue='umap')

    ch.basic_consume('umap', work)

    print("Waiting for tasks")
    ch.start_consuming()


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception:
            print(traceback.format_exc())
            continue
