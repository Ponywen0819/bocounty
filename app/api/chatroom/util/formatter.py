from flask import request
from uuid import uuid4


def format_create_payload(id):
    payload: dict = request.json

    payload['id'] = uuid4().hex
    payload['order_id'] = id
