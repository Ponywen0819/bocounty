from flask import Blueprint, request
from .util import create_order
from app.utils.response import success
from app.utils.auth.auth_util import required_login

order_api = Blueprint("order_api", __name__, url_prefix="/order")


@order_api.route("/", methods=["GET"])
@required_login()
def list():
    pass


@order_api.route("/<string:id>")
@required_login()
def get(id):
    pass


@order_api.route("/", methods=["POST"])
@required_login()
def create():
    new_id = create_order()
    return success({
        "id": new_id
    })


@order_api.route("/<string:id>")
@required_login()
def edit(id):
    pass


@order_api.route("/<string:id>")
def delete(id):
    pass
