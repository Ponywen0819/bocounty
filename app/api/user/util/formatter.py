from flask import request
from uuid import uuid4
from hashlib import sha256
from app.database.util import get


def format_create_payload():
    payload: dict = request.json
    new_id = uuid4().hex

    payload["id"] = new_id
    payload["password"] = sha256(payload["password"].encode("utf-8")).hexdigest()
    payload["bocoin"] = 0
    payload["intro"] = "留下你的自我介紹吧!"
    payload["name"] = "新進冒險者"
    payload["verify"] = 0
    payload["role"] = 0


def format_edit_payload():
    payload: dict = request.json

    password = payload.get("password")
    if password is not None:
        payload["password"] = sha256(password.encode("utf-8")).hexdigest()

    intro = payload.get("intro")
    if intro is not None:
        payload["intro"] = intro

    name = payload.get("name")
    if name is not None:
        payload["name"] = name
