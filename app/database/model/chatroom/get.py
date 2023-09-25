from app.database.util import get
from app.database.model.chatroom import Chatroom, TABLE
from app.database.model.chatroom_member import (
    get_chatroom_member_by_user_id
)
from app.utils.auth.auth_util import get_login_user


def get_chatroom_by_id(chatroom_id: str):
    chatroom_list = get(TABLE, {
        "id": chatroom_id
    })

    if len(chatroom_list) != 1:
        return None

    return Chatroom(**chatroom_list[0])


def get_user_chatroom_list():
    user = get_login_user()
    member_list = get_chatroom_member_by_user_id(user.get('id'))

    chatroom_list = []
    for member in member_list:
        chatroom = get_chatroom_by_id(member.chatroom_id)
        chatroom_list.append(chatroom)

    return chatroom_list
