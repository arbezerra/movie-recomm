from ..services import GenreService


def index():
    return [dict(row) for row in GenreService.get_all()]
