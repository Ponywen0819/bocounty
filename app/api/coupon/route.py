from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.validate import validate_buy
from .util.get import get_own_coupon, get_coupon_type
from .util.buy import buy

coupon_api = Blueprint("coupon_api", __name__, url_prefix="/coupon")


@coupon_api.route("/", methods=["GET"])
@required_login()
def get_coupon_list_api():
    coupon_types = get_coupon_type()

    return success({
        "data": coupon_types
    })


@coupon_api.route("/own", methods=["GET"])
@required_login()
def get_own_coupon_list_api():
    coupons = get_own_coupon()

    return success({
        "data": coupons
    })


@coupon_api.route("/<string:coupon_id>", methods=["POST"])
@required_login()
def buy_coupon(coupon_id: str):
    validate_buy(coupon_id)

    buy(coupon_id)

    return success()
