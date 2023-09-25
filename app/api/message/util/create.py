from flask import request
from app.database.util import create


def create_message():
    payload: dict = request.json

    create('message', payload)