from app.database.util import get
from hashlib import sha256
from app.utils.respons_util import incorrect_login_info
from werkzeug.exceptions import InternalServerError
from .validate import validate_login_payload, validate_verify_status


def get_user(payload: dict):
    validate_login_payload(payload)
    payload['password'] = sha256(payload["password"].encode("utf-8")).hexdigest()
    users = get('account', payload)
    if len(users) != 1:
        raise incorrect_login_info()

    if len(users) > 1:
        raise InternalServerError
    user = users[0]
    validate_verify_status(user)

    return user
