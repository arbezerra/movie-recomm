import pytest
import json
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def token(app):
    client = app.test_client()
    response = client.post(
        '/auth/', json={"email": "user1@example.com", "password": "123"})
    token = json.loads(response.data.decode('utf8'))
    yield token['token']
