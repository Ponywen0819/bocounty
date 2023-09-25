from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.validate import validate_order_exist
from .util.delete import delete_order

order_api = Blueprint("order_admin_api", __name__, url_prefix="/order")


@order_api.route("/<string:order_id>", methods=["DELETE"])
@required_login(required_admin=True)
def delete_order_api(order_id: str):
    validate_order_exist(order_id)

    delete_order(order_id)

    return success()
