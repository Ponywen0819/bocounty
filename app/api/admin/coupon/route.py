from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success
from .util.validate import (
    validate_create_payload,
    validate_close_time,
    validate_name,
    validate_count,
    validate_price,
    validate_describe,
    validate_coupon_exist
)
from .util.formatter import format_create_payload
from .util.get import get_list
from .util.create import create_coupon
from .util.delete import delete_coupon

coupon_api = Blueprint("admin_coupon_api", __name__, url_prefix='/coupon')


@coupon_api.route("/", methods=["GET"])
@required_login(required_admin=True)
def get_coupon_api():
    coupons = get_list()

    return success({
        "data": coupons
    })


@coupon_api.route("/", methods=["POST"])
@required_login(required_admin=True)
def create_coupon_api():
    validate_create_payload()
    validate_close_time()
    validate_name()
    validate_count()
    validate_price()
    validate_describe()

    format_create_payload()

    create_coupon()

    return success()


@coupon_api.route("/<string:coupon_id>", methods=["DElETE"])
@required_login(required_admin=True)
def delete_coupon_api(coupon_id: str):
    validate_coupon_exist(coupon_id)

    delete_coupon(coupon_id)

    return success()
