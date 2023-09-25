from app.database.util import get
from app.database.model.item import TABLE, Item


def get_item_list():
    item_list = get(TABLE)

    return [Item(**data) for data in item_list]


def get_item(item_id: str):
    item = get(TABLE, {"id": item_id})[0]

    return Item(**item)

