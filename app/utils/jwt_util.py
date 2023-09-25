from flask import current_app
import jwt


def jwt_encode(values: dict) -> str:
    secret = current_app.config["SECRET_KEY"]
    encoded: str = jwt.encode(values, secret, algorithm='HS256')
    return encoded


def jwt_decode(value: str):
    secret = current_app.config["SECRET_KEY"]
    decoded = jwt.decode(value, secret, algorithms='HS256')

    return decoded
