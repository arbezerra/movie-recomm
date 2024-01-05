def test_auth_login(app):
    client = app.test_client()
    response = client.post(
        '/auth/', json={"email": "user1@example.com", "password": "123"})
    assert response.status_code == 200


def test_auth_register(app):
    client = app.test_client()
    response = client.post(
        '/auth/register',
        json={"name": "Test", "email": "user@example.com", "password": "123"}
    )
    assert response.status_code == 200
