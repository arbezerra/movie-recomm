from ..services import MovieService


def index():
    movies = MovieService.get_all()
    return movies
