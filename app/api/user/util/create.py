from app.database.util import create
from flask import request


def create_user():
    payload: dict = request.json
    create("account", payload)

