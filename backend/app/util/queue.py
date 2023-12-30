import pika
from app import config


def connect():
    return pika.BlockingConnection(
        pika.ConnectionParameters(host=config.Q_HOST)
    )
