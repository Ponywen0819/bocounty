from flask import request
from .validate import validate_create_payload, validate_close_time, validate_exc_time, validate_close_after_exec
from app.utils.time_util import str2date


def format_create_payload():
    payload: dict = request.json
    validate_create_payload()
    validate_close_time()
    close_time = payload.get('close_time')
    payload['close_time'] = str2date(close_time).isoformat(timespec="minutes")

    validate_exc_time()
    exc_time = payload.get('exec_time')
    if exc_time is None:
        payload['exec_time'] = "None"
    else:
        payload['exec_time'] = str2date(exc_time).isoformat(timespec="minutes")

    validate_close_after_exec()

    return payload
