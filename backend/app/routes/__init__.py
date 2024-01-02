from flask import Blueprint
from .movie import movie
from .auth import auth
from .genre import genre

routes = Blueprint('routes', __name__)
routes.register_blueprint(movie, url_prefix='/movie')
routes.register_blueprint(auth, url_prefix='/auth')
routes.register_blueprint(genre, url_prefix='/genre')
