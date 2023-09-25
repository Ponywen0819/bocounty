from flask import Blueprint
from app.utils.auth.auth_util import required_login, get_login_user
from app.utils.response import success
from app.database.model.coupon import get_user_coupon_by_account_id

from .util.validate import validate_buy, validate_coupon_type_count
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
    user = get_login_user()
    coupons = get_user_coupon_by_account_id(user.get('id'))

    return success({
        "data": coupons
    })


@coupon_api.route("/<string:coupon_id>", methods=["POST"])
@required_login()
def buy_coupon(coupon_id: str):
    validate_buy(coupon_id)
    validate_coupon_type_count(coupon_id)

    buy(coupon_id)

    return success()
