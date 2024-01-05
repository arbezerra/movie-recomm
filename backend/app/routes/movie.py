from flask import Blueprint
from ..controllers.MovieController import index, star

movie = Blueprint('movie', __name__)


movie.route("/", methods=['GET'])(index)
movie.route("/<id>/star", methods=['GET', 'POST'])(star)
