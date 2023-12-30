def test_auth_login(app):
    client = app.test_client()
    response = client.post(
        '/auth/', json={"email": "user1@example.com", "password": "123"})
    assert response.status_code == 200
