from .order import CreatePayload, UpdatePayload
from .response import missing_required, wrong_format, date_in_past, close_after_exec, no_enough_coin, no_permission, \
    not_found
from app.utils.time_util import get_current, str2date
from app.utils.auth.auth_util import get_login_user
from app.utils.time_util import get_taipei_timezone
from app.database.util import get
from datetime import datetime, timedelta, timezone
from flask import request


def validate_create_payload():
    payload: dict = request.json
    try:
        CreatePayload(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()

    _validate_exc_time()
    _validate_close_time()
    _validate_close_after_exec()
    _validate_coin()


def validate_get(order_id):
    _validate_order_exist(order_id)


def validate_delete(order_id):
    _validate_order_exist(order_id)
    _validate_permission(order_id)

def _validate_order_exist(order_id: str):
    orders = get("order", {
        "id": order_id
    })

    if len(orders) != 1:
        not_found()


def _validate_exc_time():
    payload: dict = request.json
    exec_time = payload.get("exec_time")

    if exec_time is None:
        return

    if type(exec_time) != str:
        wrong_format()

    _validate_iso_format(exec_time)
    _validate_date_correct(exec_time)


def _validate_close_time():
    payload: dict = request.json
    close_time = payload.get("close_time")

    if close_time is None:
        return

    if type(close_time) != str:
        wrong_format()

    _validate_iso_format(close_time)
    _validate_date_correct(close_time)


def _validate_close_after_exec():
    payload: dict = request.json
    exec_time = payload.get("exec_time")
    if exec_time is None:
        return
    close_time = payload.get("close_time")
    if str2date(close_time) > str2date(exec_time):
        close_after_exec()


def _validate_iso_format(value: str):
    try:
        datetime.fromisoformat(value)
    except ValueError:
        raise wrong_format()


def _validate_date_correct(value: str):
    current = get_current()
    date = datetime.fromisoformat(value)
    date = date.replace(tzinfo=get_taipei_timezone())

    if date < current:
        date_in_past()


def _validate_coin():
    payload: dict = request.json

    user = get_login_user()

    if user['bocoin'] < payload["price"]:
        no_enough_coin()


def _validate_permission(order_id: str):
    user = get_login_user()
    order = get('order', {
        "id": order_id
    })[0]

    if (user["id"] != order['owner_id']) or (user['role'] == 1):
        no_permission()
