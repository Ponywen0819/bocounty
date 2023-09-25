from app.database.model.order import TABLE
from app.database.util import update


def update_order_by_id(order_id: str, values: dict):
    update(TABLE, {
        "id": order_id
    }, values)
