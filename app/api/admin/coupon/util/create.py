from app.database.util import create
from flask import request


def create_coupon():
    payload: dict = request.json

    create('coupon_type', payload)
