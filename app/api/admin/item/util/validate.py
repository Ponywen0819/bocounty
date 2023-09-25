from flask import request
from .item import CreateItem, Type
import base64

from app.utils.response import missing_required, wrong_format


def validate_create_payload():
    payload: dict = request.json

    try:
        CreateItem(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()


def validate_name():
    payload: dict = request.json

    name = payload.get('name')

    while len(name) > 0:
        if name[0] == " ":
            name = name[1:]
        else:
            break
    if name == "":
        wrong_format()


def validate_type():
    payload: dict = request.json
    try:
        Type(payload.get('type'))
    except ValueError:
        wrong_format()


def validate_photo():
    payload: dict = request.json

    base64_string = payload.get('photo').split(",")[1]

    try:
        sb_bytes = bytes(base64_string, 'ascii')
        if base64.b64encode(base64.b64decode(sb_bytes)) != sb_bytes:
            raise ValueError
    except ValueError:
        wrong_format()
