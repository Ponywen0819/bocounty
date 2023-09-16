from flask import request
from .validate import (
    validate_update_payload,
    validate_exc_time,
    validate_close_time,
    validate_close_after_exec
)
from .formatter import format_update_payload
from app.database.util import update


def update_order(id: str):
    payload: dict = request.json
    validate_update_payload(id)

    format_update_payload()
    update('order', {
        "id": id
    }, payload)






