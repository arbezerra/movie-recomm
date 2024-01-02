from flask import request
from ..services import MovieService


def index():
    page = request.args.get('page', default=1, type=int)
    limit = request.args.get('limit', default=10, type=int)
    return [dict(row) for row in MovieService.paginate(page, limit)]
