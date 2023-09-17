from flask import request
from app.utils.auth.auth_util import get_login_user
from app.utils.time_util import get_current, date2str
from uuid import uuid4

def format_create_payload(id):
    payload:dict = request.json
    user = get_login_user()

    payload['id'] = uuid4().hex
    payload['sender_id'] = user.get('id')
    payload['chatroom_id'] = id
    payload['content'] = remove_space( payload['content'])
    payload['time'] = date2str(get_current())


def remove_space(value: str):
    while len(value) > 0:
        if value[0] == " ":
            value = value[1:]
        else:
            break
    return value