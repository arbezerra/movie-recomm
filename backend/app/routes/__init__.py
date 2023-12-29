from flask import Blueprint
from .movie import movie
from .auth import auth

routes = Blueprint('routes', __name__)
routes.register_blueprint(movie, url_prefix='/movie')
routes.register_blueprint(auth, url_prefix='/auth')
