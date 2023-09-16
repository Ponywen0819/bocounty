from .order import CreatePayload, UpdatePayload
from .response import missing_required, wrong_format, date_in_past, close_after_exec, no_enough_coin, no_permission
from app.utils.time_util import get_current, str2date
from app.utils.auth.auth_util import get_login_user
from app.utils.time_util import get_taipei_timezone
from app.database.util import get
from datetime import datetime, timedelta, timezone
from flask import request


def validate_create_payload():
    payload: dict = request.json
    try:
        print(payload)
        CreatePayload(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()

    if payload.get("exec_time"):
        validate_exc_time()

    validate_close_time()
    validate_close_after_exec()
    validate_coin()


def validate_update_payload(id: str):
    payload: dict = request.json
    try:
        UpdatePayload(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()

    if payload.get("exec_time"):
        validate_exc_time()

    validate_close_time()
    validate_close_after_exec()
    validate_permission(id)


def validate_exc_time():
    payload: dict = request.json
    exec_time = payload.get("exec_time")

    if type(exec_time) != str:
        wrong_format()

    validate_iso_format(exec_time)
    validate_date_correct(exec_time)


def validate_close_time():
    payload: dict = request.json
    close_time = payload.get("close_time")

    if type(close_time) != str:
        wrong_format()

    validate_iso_format(close_time)
    validate_date_correct(close_time)


def validate_close_after_exec():
    payload: dict = request.json
    exec_time = payload.get("exec_time")
    if exec_time is None:
        return
    close_time = payload.get("close_time")
    if str2date(close_time) > str2date(exec_time):
        close_after_exec()


def validate_iso_format(value: str):
    try:
        datetime.fromisoformat(value)
    except ValueError:
        raise wrong_format()


def validate_date_correct(value: str):
    current = get_current()
    date = datetime.fromisoformat(value)
    date = date.replace(tzinfo=get_taipei_timezone())

    if date < current:
        date_in_past()


def validate_coin():
    payload: dict = request.json

    user = get_login_user()

    if user['bocoin'] < payload["price"]:
        no_enough_coin()


def validate_permission(id: str):
    user = get_login_user()
    order = get('order', {
        "id": id
    })[0]

    if (user["id"] != order['owner_id']) or (user['role'] == 1):
        no_permission()
