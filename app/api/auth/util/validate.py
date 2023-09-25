from .response import missing_required, wrong_format, not_verified
from flask import request
from app.database.util import get
from hashlib import sha256
from .response import incorrect
from .payload import LoginPayload


def validate_login_payload():
    payload: dict = request.json
    try:
        LoginPayload(**payload)
    except ValueError:
        wrong_format()
    except TypeError:
        missing_required()


def validate_password_correct():
    payload: dict = request.json

    payload['password'] = sha256(payload["password"].encode("utf-8")).hexdigest()
    users = get('account', payload)
    if len(users) != 1:
        incorrect()

    return users[0]


def validate_verify_status(user: dict):
    if user.get("verify") == 0:
        not_verified()
