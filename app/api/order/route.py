from flask import Blueprint, jsonify
from .util import create_order, get_order_list, get_order
from .util.update import update_order
from .util.delete import delete_order
from app.utils.response import success
from app.utils.auth.auth_util import required_login

order_api = Blueprint("order_api", __name__, url_prefix="/order")


@order_api.route("/", methods=["GET"])
@required_login()
def list():
    orders = get_order_list()
    return success({
        "orders": orders
    })


@order_api.route("/<string:id>", methods=["GET"])
@required_login()
def get(id):
    order = get_order(id)

    return success({
        "order": order
    })


@order_api.route("/", methods=["POST"])
@required_login()
def create():
    new_id = create_order()
    return success({
        "id": new_id
    })


@order_api.route("/<string:id>", methods=["PUT"])
@required_login()
def edit(id):
    order = get_order(id)
    update_order(id)

    return success()


@order_api.route("/<string:id>", methods=["DELETE"])
def delete(id):
    order = get_order(id)
    delete_order(id)
    return success()



