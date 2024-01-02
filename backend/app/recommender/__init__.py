import pandas as pd
from .svc import SVC


class Recommender:
    def __init__(self):
        self.SVC_MIN = 3
        self.svc = SVC()

    def init_app(self, service):
        self.service = service

    def recommend(self, user_id):
        map = pd.DataFrame(self.service.get_map(), columns=["id", "x", "y"])
        stared = pd.DataFrame(self.service.get_stared(
            user_id), columns=["user_id", "movie_id", "stars"])
        star_map = pd.merge(
            map,
            stared,
            left_on="id",
            right_on="movie_id",
            how="right"
        )

        if star_map.shape[0] < self.SVC_MIN:
            return self.service.paginate(1, 10)

        recommendations = self.svc.select(map, star_map)

        ids = tuple(row['id']
                    for index, row in recommendations.head(10).iterrows())
        movies = list(self.service.get_by_ids(ids))
        order = {val: index for index, val in enumerate(ids)}
        movies.sort(key=lambda x: order[x['id']])

        return movies
