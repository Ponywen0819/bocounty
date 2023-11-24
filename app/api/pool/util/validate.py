from app.database.util import get
from app.utils.response import not_found


def validate_pool_itme(pool_id: str):
    _validate_pool_exist(pool_id)


def validate_draw(pool_id: str):
    _validate_pool_exist(pool_id)

def _validate_pool_exist(pool_id: str):
    pool_list = get('pool', {
        "id": pool_id
    })

    if len(pool_list) != 1:
        not_found('pool not found')