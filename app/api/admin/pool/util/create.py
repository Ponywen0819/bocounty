from app.database.util import create
from flask import request
import base64
from uuid import uuid4
from os import path, getcwd


def create_pool():
    payload: dict = request.json

    create('pool', payload)


def save_photo():
    payload: dict = request.json

    metadata, base64_string = payload.get('photo').split(",")

    file_metadata = metadata.split(";")[0]

    file_format = file_metadata.split("/")[1]

    imgdata = base64.b64decode(base64_string)

    file_name = f"{uuid4().hex}.{file_format}"
    file_path = path.join(getcwd(), "public", file_name)
    with open(file_path, 'wb') as f:
        f.write(imgdata)

    payload["photo"] = f"/static/{file_name}"
