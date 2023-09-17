from app.utils.auth.auth_util import get_login_user
from app.database.util import create, update
from uuid import uuid4
from flask import request


def create_order():
    payload: dict = request.json

    create('order', payload)

    user = get_login_user()

    update('account', {
        "id": user["id"]
    }, {
        "bocoin": user["bocoin"] - payload['price']
    })


def generate_create_payload():
    payload: dict = request.json
    new_id = uuid4().hex
    user = get_login_user()
