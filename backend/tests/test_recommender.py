
def test_recommender(app, token):
    client = app.test_client()
    response = client.post(
        '/recommend', headers={'Authorization': f"Bearer {token}"})
    assert response.status_code == 200
