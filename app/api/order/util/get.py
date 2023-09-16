from app.database.util import get
from .order import Order
from .response import not_found, conflict_id
from werkzeug.exceptions import InternalServerError


def get_order_list():
    orders = get('order')
    return [Order(**order) for order in orders]


def get_order(id):
    orders = get('order', {
        "id": id
    })

    if len(orders) < 1:
        not_found()

    if len(orders) != 1:
        conflict_id()

    return Order(**orders[0])
