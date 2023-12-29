from flask import Blueprint
from ..controllers.AuthController import login

auth = Blueprint('auth', __name__)

auth.route("/", methods=['POST'])(login)
