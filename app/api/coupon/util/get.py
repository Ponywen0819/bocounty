from .coupon import Coupon, CouponType
from app.database.util import get, delete
from app.utils.auth.auth_util import get_login_user


def get_own_coupon():
    user = get_login_user()

    coupons = get("coupon_summary", {
        "owner_id": user.get('id')
    })

    return [Coupon(**data) for data in coupons]


def get_coupon_type():
    delete("coupon_type", {
        "count": 0
    })

    coupon_types = get('coupon_type')

    return [CouponType(**data) for data in coupon_types]
