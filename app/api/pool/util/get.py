from app.database.util import get
from .pool import Pool, PoolItem

def get_pool_list():
    pool_list = get('pool')

    return [Pool(**data) for data in pool_list]


def get_pool_item(pool_id: str):
    item_list = get('pool_item', {
        "pool_id": pool_id
    })

    return [PoolItem(**data) for data in item_list]

