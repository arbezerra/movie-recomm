from flask import Blueprint
from .movie import movie

routes = Blueprint('routes', __name__)
routes.register_blueprint(movie, url_prefix='/movie')
