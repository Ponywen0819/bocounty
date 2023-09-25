from flask import Blueprint
from .util.validate import (
    validate_create_payload,
    validate_get,
    validate_delete,
    validate_exc_time,
    validate_close_time,
    validate_close_after_exec,
    validate_coin
)
from .util.formatter import format_create_payload
from .util.get import get_open_order, get_enrolled_order, get_order
from .util.create import create_order
from .util.delete import delete_order
from .util.checker import check_order

from app.utils.response import success
from app.utils.auth.auth_util import required_login

order_api = Blueprint("order_api", __name__, url_prefix="/order")


@order_api.route("/", methods=["POST"])
@required_login()
def create():
    check_order()

    validate_create_payload()
    validate_exc_time()
    validate_close_time()
    validate_close_after_exec()
    validate_coin()

    format_create_payload()

    create_order()

    return success()


@order_api.route("/open", methods=["GET"])
@required_login()
def list_open():
    check_order()
    orders = get_open_order()

    return success({
        "data": orders
    })


@order_api.route("/enrolled", methods=["GET"])
@required_login()
def list_enrolled():
    check_order()
    orders = get_enrolled_order()
    return success({
        "data": orders
    })


@order_api.route("/<string:order_id>", methods=["GET"])
@required_login()
def get(order_id: str):
    validate_get(order_id)
    order = get_order(order_id)
    return success({
        "data": order
    })


@order_api.route("/<string:order_id>", methods=["DELETE"])
@required_login()
def delete(order_id: str):
    validate_delete(order_id)
    delete_order(order_id)
    return success()
