from flask import request
from .message import CreateMessage
from .response import not_valid_member
from app.utils.auth.auth_util import get_login_user
from app.utils.response import missing_required, wrong_format, not_found
from app.database.util import get


def validate_create_payload(id: str):
    payload: dict = request.json
    try:
        CreateMessage(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()
    _validate_chatroom_exist(id)
    _validate_valid_member(id)


def validate_get(id: str):
    _validate_chatroom_exist(id)
    _validate_valid_member(id)

def _validate_chatroom_exist(id: str):
    chatroom_list = get('chatroom', {
        "id": id
    })

    if len(chatroom_list) != 1:
        not_found('chatroom not found')


def _validate_valid_member(id):
    user = get_login_user()
    chatroom_list = get('chatroom_summary', {
        'account_id': user.get('id'),
        "id": id
    })

    if len(chatroom_list) != 1:
        not_valid_member()
