from datetime import datetime, timedelta, timezone
from .validate import validate_create_payload, validate_close_time, validate_exc_time
from uuid import uuid4
from .order import Order


def create_order(payload: dict):
    validate_create_payload(payload)
    validate_close_time(payload)
    validate_exc_time(payload)

    new_id = uuid4().hex
    new_order = Order(**{
        "id": new_id,
        "status": 0,
        "owner_id": "1",
        **payload,
        "start_time": datetime.now(tz=timezone(timedelta(hours=8)))
    })

    print(new_order)
    return new_id
