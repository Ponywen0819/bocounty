from .order import CreatePayload
from .response import missing_required, wrong_format, date_in_past, close_after_exec, no_enough_coin
from app.utils.time_util import get_current, str2date
from datetime import datetime, timedelta, timezone
from flask import request


def validate_create_payload():
    payload: dict = request.json
    required_columns = _get_required_column()
    for key in required_columns:
        value = payload.get(key)
        if (value is None) and (type(value) != required_columns.get(key)):
            print(key)
            missing_required()


def validate_exc_time():
    payload: dict = request.json
    exc_time = payload.get("exec_time")

    if exc_time is None:
        return

    if type(exc_time) != str:
        wrong_format()

    validate_iso_format(exc_time)
    date = str2date(exc_time)
    validate_date_correct(date)


def validate_close_time():
    payload: dict = request.json
    close_time = payload.get("close_time")

    if close_time is None:
        missing_required()

    if type(close_time) != str:
        wrong_format()

    validate_iso_format(close_time)
    date = str2date(close_time)
    validate_date_correct(date)


def validate_close_after_exec():
    payload: dict = request.json
    exc_time = payload.get("exec_time")
    if exc_time == "None":
        return
    close_time = payload.get("close_time")
    if str2date(close_time) > str2date(exc_time):
        close_after_exec()


def validate_iso_format(value: str):
    try:
        datetime.fromisoformat(value)
    except ValueError:
        raise wrong_format()


def validate_date_correct(value: datetime):
    current = get_current()

    if value < current:
        date_in_past()


def validate_coin(user: dict):
    payload: dict = request.json
    if user['bocoin'] < payload["price"]:
        no_enough_coin()

def _get_required_column():
    user_columns: dict = CreatePayload.__dict__["__annotations__"]
    return user_columns
