from __future__ import annotations

from app.database.util import get
from app.database.model.order import TABLE, Order


def get_order_by_id(order_id: str) -> Order | None:
    order_list = get(TABLE, {"id": order_id})

    if len(order_list) != 1:
        return

    return Order(**order_list[0])
