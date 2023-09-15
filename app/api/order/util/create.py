from datetime import datetime
from .validate import validate_create_payload
from uuid import uuid4


def create_order(payload: dict):
    validate_create_payload(payload)

    new_id = uuid4()

    return new_id
