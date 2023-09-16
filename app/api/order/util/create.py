from app.utils.auth.auth_util import get_login_user
from app.utils.time_util import get_current
from app.database.util import create, update
from uuid import uuid4
from .formatter import format_create_payload
from .validate import validate_create_payload
from flask import request


def create_order():
    payload: dict = request.json
    validate_create_payload()

    format_create_payload()
    generate_create_payload()

    pay()
    create('order', payload)

    return payload.get('id')


def generate_create_payload():
    payload: dict = request.json
    new_id = uuid4().hex
    user = get_login_user()

    payload["id"] = new_id
    payload["status"] = 0
    payload["owner_id"] = user.get('id')
    payload["start_time"] = get_current().isoformat(timespec='minutes')


def pay():
    payload: dict = request.json
    user = get_login_user()

    update('account', {
        "id": user["id"]
    }, {
        "bocoin": user["bocoin"] - payload['price']
    })
