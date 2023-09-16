from functools import wraps
from flask import request
from app.utils.jwt_util import jwt_decode
from app.database.util import get
from .response import not_login, no_permission


def required_login(required_admin=False):
    def generator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            decoded = get_jwt_data()
            id = decoded.get("id")

            user = get_user(id)

            if required_admin:
                role = user.get("role")
                if role is None or role == 0:
                    no_permission()
            return func(*args, **kwargs)

        return wrapper

    return generator


def get_jwt_data() -> dict:
    user_token: str = request.cookies['user_token']
    if user_token is None:
        not_login()

    try:
        decoded = jwt_decode(user_token)
    except:
        not_login()

    return decoded


def get_user(id: str):
    users = get('account', {
        "id": id
    })
    if len(users) != 1:
        not_login()

    return users[0]
