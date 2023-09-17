from flask import request
from app.database.util import create, get
from app.utils.auth.auth_util import get_login_user


def create_chatroom(payload: dict):
    create("chatroom", payload)


def initial_member(payload: dict):
    order = get('order', {
        "id": payload.get('order_id')
    })[0]
    create("chatroom_member", {
        "chatroom_id": payload.get('id'),
        "account_id": order.get('owner_id')
    })

    user = get_login_user()
    create("chatroom_member", {
        "chatroom_id": payload.get('id'),
        "account_id": user.get('id')
    })
