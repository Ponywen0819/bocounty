from .order import Order
from .response import missing_required, wrong_format
from datetime import datetime


def validate_create_payload(payload: dict):
    required_columns = _get_required_column()
    for key in required_columns:
        value = payload.get(key)
        if (value is None) and (type(value) != required_columns.get(key)):
            missing_required()


def validate_iso_format(value: str):
    try:
        datetime.fromisoformat(value)
    except ValueError:
        raise wrong_format()


def _get_required_column():
    user_columns: dict = Order.__dict__["__annotations__"]
    return {
        "title": user_columns['title'],
        "close_time": user_columns['close_time'],
        "exc_time": user_columns['exc_time'],
        "price": user_columns['price'],
        "intro": user_columns['intro']
    }
