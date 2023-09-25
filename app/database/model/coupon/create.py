from app.database.util import create
from app.database.model.coupon import TABLE
from uuid import uuid4


def create_coupon(account_id: str, type_id: str):
    new_id = uuid4().hex
    create(TABLE, {
        "id": new_id,
        "type_id": type_id,
        "owner_id": account_id
    })
