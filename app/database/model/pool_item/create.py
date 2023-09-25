from app.database.model.pool_item import TABLE
from app.database.util import create


def create_pool_item(pool_id: str, item_id: str):
    create(TABLE,{
        "pool_id": pool_id,
        "item_id": item_id
    })