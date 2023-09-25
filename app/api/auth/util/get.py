from app.database.util import get
from hashlib import sha256
from werkzeug.exceptions import InternalServerError
from .response import incorrect
from .validate import validate_login_payload, validate_verify_status


def get_user(payload: dict):
    validate_login_payload(payload)
    payload['password'] = sha256(payload["password"].encode("utf-8")).hexdigest()
    users = get('account', payload)
    if len(users) != 1:
        incorrect()

    user = users[0]
    validate_verify_status(user)

    return user
