from flask import request
from app.database.util import get
from app.utils.response import not_found


def validate_order_exist(order_id:str):
    order_list = get('order',{"id": order_id})

    if len(order_list) != 1:
        not_found()

