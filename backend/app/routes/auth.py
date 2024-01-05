from flask import Blueprint
from ..controllers.AuthController import login, register

auth = Blueprint('auth', __name__)

auth.route("/", methods=['POST'])(login)
auth.route("/register", methods=['POST'])(register)
