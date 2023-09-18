from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.validate import (
    validate_create_payload,
    validate_name,
    validate_photo,
    validate_close_time
)
from .util.formatter import format_create_payload
from .util.get import get_pool_list
from .util.create import save_photo, create_pool

pool_api = Blueprint("pool_admin_api", __name__, url_prefix='/pool')


@pool_api.route("/", methods=["GET"])
@required_login(required_admin=True)
def get_pool_api():
    pools = get_pool_list()

    return success({
        "data": pools
    })


@pool_api.route("/", methods=["POST"])
@required_login(required_admin=True)
def create_pool_api():
    validate_create_payload()
    validate_photo()
    validate_name()
    validate_close_time()

    format_create_payload()

    save_photo()
    create_pool()

    return success()
