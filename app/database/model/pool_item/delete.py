from app.database.model.pool_item import TABLE
from app.database.util import delete


def delete_by_id(pool_id: str, item_id: str):
    delete(TABLE, {
        "pool_id": pool_id,
        "item_id": item_id
    })
