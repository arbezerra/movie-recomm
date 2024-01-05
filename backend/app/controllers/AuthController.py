from flask import request
from app import config
from ..services import UserService
from ..util.hash import verify, hash
import jwt
import datetime


def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = UserService.by_email(email)
    if not user or not verify(password, user['password']):
        return {"msg": "User or Password do not match"}, 403

    token = jwt.encode({
        'id': user['id'],
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=30),
    }, config.JWT_SECRET, algorithm="HS256")
    return {'token': token}


def register():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')

    user = UserService.by_email(email)
    if user:
        return {"msg": "User already exists"}, 422

    user = UserService.insert({
        'name': name,
        'email': email,
        'password': hash(password),
    })

    if not user:
        return {"msg": "Error! Could not create the user"}, 422

    token = jwt.encode({
        'id': user['id'],
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=30),
    }, config.JWT_SECRET, algorithm="HS256")

    return {'token': token}
