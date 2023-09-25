from app.database.util import get
from app.database.model.pool_item import TABLE, PoolItem
from app.database.model.item import get_item


def get_pool_item(pool_id: str):
    item_list = get(TABLE, {
        "pool_id": pool_id
    })

    res = []
    for item_record in item_list:
        item = get_item(item_record.get("item_id"))
        res.append(item)

    return res
