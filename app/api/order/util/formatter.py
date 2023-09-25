from flask import request
from app.utils.time_util import str2date, date2str, get_current, format
from app.utils.auth.auth_util import get_login_user
from app.database.model.order import OrderStatus
from uuid import uuid4


def format_create_payload():
    payload: dict = request.json

    new_id = uuid4().hex
    user = get_login_user()

    payload["id"] = new_id
    payload["status"] = OrderStatus.RECRUITING.value
    payload["owner_id"] = user.get('id')
    payload["start_time"] = date2str(get_current())
    payload['close_time'] = format(payload.get('close_time'))

    exc_time = payload.get('exec_time')
    if exc_time != "None":
        payload['exec_time'] = format(exc_time)


def format_update_payload():
    payload: dict = request.json

    payload['close_time'] = format_datetime(payload.get('close_time'))

    exc_time = payload.get('exec_time')
    if exc_time is None:
        payload['exec_time'] = "None"
    else:
        payload['exec_time'] = format_datetime(exc_time)

    return payload


def format_datetime(string: str) -> str:
    return str2date(string).isoformat(timespec="minutes")
