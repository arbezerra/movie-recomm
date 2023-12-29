from app import config
import requests


class API:
    def __init__(self):
        self.URL = "https://api.themoviedb.org/3"
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {config.TMDB_TOKEN}",
        }

    def get(self, uri):
        response = requests.get(self.URL + uri, headers=self.headers)
        print(response.encoding)
        result = response.json()
        return result
