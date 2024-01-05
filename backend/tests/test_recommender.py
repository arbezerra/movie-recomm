import time


def test_recommender(app, token):
    client = app.test_client()
    # Wait for UMAP
    time.sleep(30)
    response = client.post(
        '/recommend', headers={'Authorization': f"Bearer {token}"})
    assert response.status_code == 200
