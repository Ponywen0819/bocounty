from .pool import CreatePool, UpdatePool
from flask import request
from app.utils.response import missing_required, wrong_format, not_found
from app.utils.time_util import get_current, str2date
from app.database.util import get

import base64
from datetime import datetime
from .response import date_in_past, item_in_pool


def validate_create_payload():
    payload: dict = request.json
    try:
        CreatePool(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()


def validate_update_payload():
    payload: dict = request.json
    try:
        UpdatePool(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()


def validate_close_time():
    payload: dict = request.json

    close_time = payload.get("close_time")

    if close_time is None:
        return

    _validate_iso_format(close_time)
    _validate_date_correct(close_time)


def validate_photo():
    payload: dict = request.json

    photo = payload.get('photo')

    if photo is None:
        return

    base64_string = photo.split(",")[1]

    try:
        sb_bytes = bytes(base64_string, 'ascii')
        if base64.b64encode(base64.b64decode(sb_bytes)) != sb_bytes:
            raise ValueError
    except ValueError:
        wrong_format()


def validate_name():
    payload: dict = request.json

    name = payload.get('name')

    if name is None:
        return

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


def validate_pool_exist(pool_id: str):
    pools = get('pool', {
        "id": pool_id
    })

    if len(pools) != 1:
        not_found('pool not found')

def validate_item_exist(item_id: str):
    item = get('item',{"id": item_id})

    if len(item) != 1:
        not_found('item not exist')

def validate_item_in_pool(pool_id: str, item_id: str):
    pools = get('pool_item', {
        "pool_id": pool_id,
        "item_id": item_id
    })

    if len(pools) != 1:
        not_found('item not in pool')


def validate_item_not_in_pool(pool_id: str, item_id: str):
    pools = get('pool_item', {
        "pool_id": pool_id,
        "item_id": item_id
    })

    if len(pools) != 0:
        item_in_pool()
