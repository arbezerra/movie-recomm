import string
import random

def test_auth_login(app):
    client = app.test_client()
    response = client.post(
        '/auth/', json={"email": "user1@example.com", "password": "123"})
    assert response.status_code == 200


def test_auth_register(app):
    client = app.test_client()
    email = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(20))
    response = client.post(
        '/auth/register',
        json={"name": "Test", "email": f"{email}@example.com", "password": "123"}
    )
    assert response.status_code == 200
