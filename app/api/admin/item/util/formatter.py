from flask import request
from uuid import uuid4

def format_create_payload():
    payload: dict = request.json
    new_id = uuid4().hex

    payload["id"] = new_id

