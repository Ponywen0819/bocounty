from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success
from .util.validate import (
    validate_create_payload,
    validate_close_time,
    validate_name,
    validate_count,
    validate_price,
    validate_describe
)
from .util.formatter import format_create_payload
from .util.create import create_coupon

coupon_api = Blueprint("admin_coupon_api", __name__, url_prefix='/coupon')


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
