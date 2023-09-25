from app.database.util import update
from app.database.model.account import TABLE


def update_account_by_id(account_id: str, values: dict):
    update(TABLE, {"id": account_id}, values)
