from flask import request
from .report import CreateReport, Type
from .response import self_report, reported
from app.utils.response import missing_required, wrong_format, not_found
from app.utils.auth.auth_util import get_login_user
from app.database.util import get


def validate_create_payload(order_id: str):
    payload: dict = request.json
    try:
        CreateReport(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()

    _validate_order_exist(order_id)
    _validate_self_report(order_id)
    _validate_create_type()


def _validate_order_exist(id: str):
    payload: dict = request.json
    orders = get('order', {
        "id": id
    })

    if len(orders) != 1:
        not_found('order not found')


def _validate_self_report(order_id: str):
    order = get('order', {
        "id": order_id
    })[0]

    user = get_login_user()

    if order.get('owner_id') == user.get('id'):
        self_report()


def _validate_create_type():
    payload: dict = request.json
    try:
        Type(payload.get("type"))
    except ValueError:
        wrong_format("unknown report type")


def validate_not_reported(order_id: str):
    user = get_login_user()
    report_list = get('report', {
        "publisher_id": user.get('id'),
        "order_id": order_id
    })

    if len(report_list) != 0:
        reported()
