from app.database.util import get, get_db
from app.utils.response import not_found
from .response import already_exist, not_owner, not_member, is_owner
from app.utils.auth.auth_util import get_login_user


def validate_create_payload(order_id: str):
    _validate_order_exist(order_id)
    _validate_conflict(order_id)
    _validate_user(order_id)


def validate_assign(chatroom_id: str):
    _validate_chatroom_exist(chatroom_id)
    _validate_owner(chatroom_id)


def validate_member(chatroom_id: str):
    _validate_chatroom_exist(chatroom_id)


def _validate_conflict(id):
    user = get_login_user()

    chatroom_list = get('chatroom_summary', {
        "account_id": user.get('id'),
        "order_id": id
    })

    if len(chatroom_list) != 0:
        already_exist()


def _validate_order_exist(id):
    orders = get('order', {
        "id": id
    })

    if len(orders) != 1:
        not_found('order not found')


def _validate_chatroom_exist(chatroom_id: str):
    chatroom_list = get("chatroom", {
        "id": chatroom_id
    })

    if len(chatroom_list) != 1:
        not_found('chatroom not found')


def _validate_user(order_id: str):
    user = get_login_user()
    orders = get('order', {
        "id": order_id,
        "owner_id": user.get('id')
    })

    if len(orders) != 0:
        is_owner()


def _validate_owner(chatroom_id: str):
    user = get_login_user()

    chatroom_list = get('chatroom_summary', {
        "id": chatroom_id,
        "account_id": user.get('id')
    })

    if len(chatroom_list) != 1:
        not_member()

    orders = get('order', {
        "owner_id": user.get('id'),
        "id": chatroom_list[0].get('order_id')
    })

    if len(orders) != 1:
        not_owner()
