from flask import request
from app.database.util import get
from app.utils.auth.auth_util import get_login_user
from .chatroom import Chatroom

def get_chatroom_list():
    user = get_login_user()
    chatroom_list = get("chatroom_summary", {
        "account_id": user.get('id')
    })

    return [ Chatroom(**data) for data in chatroom_list]
