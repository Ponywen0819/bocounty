from app.utils.auth.auth_util import get_jwt_data, get_user
from app.utils.time_util import get_current
from app.database.util import create, update
from uuid import uuid4
from .formatter import format_create_payload
from .validate import validate_coin
from flask import request


def create_order():
    payload = format_create_payload()
    payload = generate_create_payload(payload)

    pay()
    create('order', payload)

    return payload.get('id')


def generate_create_payload(payload: dict):
    new_id = uuid4().hex
    user = get_login_user()

    return {
        "id": new_id,
        "status": 0,
        "owner_id": user.get('id'),
        **payload,
        "start_time": get_current().isoformat(timespec='minutes')
    }


def pay():
    payload: dict = request.json
    user = get_login_user()
    validate_coin(user)

    update('account', {
        "id": user["id"]
    }, {
        "bocoin": user["bocoin"] - payload['price']
    })


def get_login_user():
    data = get_jwt_data()
    user = get_user(data.get('id'))
    return user
