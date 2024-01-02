from flask import Blueprint
from ..controllers.GenreController import index

genre = Blueprint('genre', __name__)

genre.route("/", methods=['GET'])(index)
