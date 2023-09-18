from .pool import CreatePool
from flask import request
from app.utils.response import missing_required, wrong_format
from app.utils.time_util import get_current, str2date

import base64
from datetime import datetime
from .response import date_in_past



def validate_create_payload():
    payload: dict = request.json
    try:
        CreatePool(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()


def validate_close_time():
    payload: dict = request.json

    close_time = payload.get("close_time")

    if close_time is None:
        return

    if type(close_time) != str:
        wrong_format()

    _validate_iso_format(close_time)
    _validate_date_correct(close_time)


def validate_photo():
    payload: dict = request.json

    base64_string = payload.get('photo').split(",")[1]

    try:
        sb_bytes = bytes(base64_string, 'ascii')
        if base64.b64encode(base64.b64decode(sb_bytes)) != sb_bytes:
            raise ValueError
    except ValueError:
        wrong_format()


def validate_name():
    payload: dict = request.json

    name = payload.get('name')

    while len(name) > 0:
        if name[0] == " ":
            name = name[1:]
        else:
            break
    if name == "":
        wrong_format()


def _validate_iso_format(value: str):
    try:
        datetime.fromisoformat(value)
    except ValueError:
        raise wrong_format()


def _validate_date_correct(value: str):
    current = get_current()
    date = str2date(value)

    if date < current:
        date_in_past()
