from flask import request
from .report import CreateReport, Type
from app.utils.response import missing_required, wrong_format, not_found
from app.database.util import get


def validate_create_payload(id: str):
    payload: dict = request.json
    try:
        CreateReport(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()

    _validate_create_order(id)
    _validate_create_type()


def _validate_create_order(id: str):
    payload: dict = request.json
    orders = get('order', {
        "id": id
    })

    if len(orders) != 1:
        not_found('order not found')


def _validate_create_type():
    payload: dict = request.json
    try:
        Type(payload.get("type"))
    except ValueError:
        wrong_format("unknown report type")
