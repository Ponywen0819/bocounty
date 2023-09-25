from app.database.util import get
from .coupon import Coupon


def get_list():
    coupons = get('coupon_type')

    return [Coupon(**data) for data in coupons]
