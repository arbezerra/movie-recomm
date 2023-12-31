from flask import request
from app import config
from ..services import UserService
from ..util.hash import verify
import jwt
import datetime


def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = UserService.by_email(email)
    print(user)
    if not user or not verify(password, user['password']):
        return {"msg": "User or Password do not match"}, 403

    return jwt.encode({
        'id': user['id'],
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=30),
    }, config.JWT_SECRET, algorithm="HS256")
