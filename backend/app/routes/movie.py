from flask import Blueprint
from ..controllers.MovieController import index

movie = Blueprint('movie', __name__)


movie.route("/", methods=['GET'])(index)
