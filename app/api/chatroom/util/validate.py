from app.database.util import get, get_db
from app.utils.response import not_found
from .response import already_exist, not_owner, not_member, is_owner
from app.utils.auth.auth_util import get_login_user
from app.database.model.chatroom import ChatroomStatus
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


def validate_complete(chatroom_id: str):
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


def validate_chatroom_exist(chatroom_id: str):
    chatroom_list = get("chatroom", {
        "id": chatroom_id
    })

    if len(chatroom_list) != 1:
        not_found('chatroom not found')


def validate_is_member(chatroom_id: str):
    user = get_login_user()

    chatroom_members = get('chatroom_member', {
        "chatroom_id": chatroom_id
    })

    for chatroom_member in chatroom_members:
        account_id = chatroom_member.get('account_id')
        if account_id == user.get('id'):
            return

    not_member()


def validate_not_owner(chatroom_id: str):
    user = get_login_user()

    chatroom = get('chatroom', {
        "id": chatroom_id
    })[0]

    order = get('order', {
        "id": chatroom.get('order_id')
    })[0]

    if user.get('id') == order.get('owner_id'):
        is_owner()


def validate_is_owner(chatroom_id: str):
    user = get_login_user()

    chatroom = get('chatroom', {
        "id": chatroom_id
    })[0]

    order = get('order', {
        "id": chatroom.get('order_id')
    })[0]

    if user.get('id') != order.get('owner_id'):
        not_owner()


def validate_not_recruiting(chatroom_id: str):
    chatroom = get('chatroom', {
        "id": chatroom_id
    })[0]

    if ChatroomStatus(chatroom.get('status')) != ChatroomStatus.RECRUITING:
        already_exist("user already been assigned")


def validate_not_submit(chatroom_id: str):
    chatroom = get('chatroom', {
        "id": chatroom_id
    })[0]

    if ChatroomStatus(chatroom.get('status')) != ChatroomStatus.NORMAL:
        already_exist("user already submitted or finished")


def validate_not_finish(chatroom_id: str):
    chatroom = get('chatroom', {
        "id": chatroom_id
    })[0]

    if ChatroomStatus(chatroom.get('status')) == ChatroomStatus.CONFIRM:
        already_exist("user already finished")
