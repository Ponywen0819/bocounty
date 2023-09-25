from app.utils.time_util import get_current, date2str, format
from app.utils.auth.auth_util import get_login_user
from flask import request
from uuid import uuid4


def format_create_payload():
    payload: dict = request.json

    new_id = uuid4().hex
    current = date2str(get_current())
    user = get_login_user()

    payload['id'] = new_id
    payload['start_time'] = current
    payload['close_time'] = format(payload['close_time'])
    payload['publisher_id'] = user.get('id')
    payload['name'] = str_format(payload['name'])
    payload['describe'] = str_format(payload['describe'])


def str_format(string: str):
    while len(string) > 0:
        if string[0] == " ":
            string = string[1:]
        else:
            break

    return string
