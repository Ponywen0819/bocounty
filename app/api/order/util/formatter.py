from flask import request
from app.utils.time_util import str2date


def format_create_payload():
    payload: dict = request.json

    payload['close_time'] = format_datetime(payload.get('close_time'))

    exc_time = payload.get('exec_time')
    if exc_time is None:
        payload['exec_time'] = "None"
    else:
        payload['exec_time'] = format_datetime(exc_time)

    return payload


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
