from flask import request
from ..services import MovieService
from app.util import auth


def index():
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    return [dict(row) for row in MovieService.paginate(page, limit)]


def star(id):
    bearer = request.headers.get('Authorization')
    token = auth.verify(bearer)
    if not token:
        return {'message': 'Forbidden'}, 403
    stars = request.json.get('stars')
    result = MovieService.star(id, token['id'], stars)

    if not result:
        return {'message': 'Error'}, 422
    return {'message': 'ok'}
