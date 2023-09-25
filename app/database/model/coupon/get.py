from app.database.util import get
from app.database.model.coupon import TABLE, Coupon


def get_user_coupon_by_account_id(account_id):
    coupon_list = get(TABLE, {"owner_id": account_id})

    return [Coupon(**data) for data in coupon_list]
