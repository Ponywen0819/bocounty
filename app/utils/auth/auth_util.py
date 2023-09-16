from functools import wraps
from flask import request
from app.utils.jwt_util import jwt_decode
from app.database.util import get
from .response import not_login, no_permission


def required_login(required_admin=False):
    def generator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_token: str = request.cookies['user_token']
            if user_token is None:
                not_login()

            try:
                decoded = jwt_decode(user_token)
            except:
                not_login()

            id = decoded.get("id")
            users = get('account', {
                "id": id
            })
            if len(users) != 1:
                not_login()
            if required_admin:
                role = users[0].get("role")
                if role is None or role == 0:
                    no_permission()
            return func(*args, **kwargs)

        return wrapper

    return generator
