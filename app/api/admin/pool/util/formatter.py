from flask import request
from uuid import uuid4
from app.utils.time_util import get_current, date2str


def format_create_payload():
    payload: dict = request.json

    payload['id'] = uuid4().hex
    payload['start_time'] = date2str(get_current())
    close_time = payload.get('close_time')
    if close_time is None:
        payload['close_time'] = "None"
