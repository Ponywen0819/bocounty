from flask import Blueprint, request
from .util import create_order
from app.utils.response import success

order_api = Blueprint("order_api", __name__, url_prefix="/order")


@order_api.route("/", methods=["GET"])
def list():
    pass


@order_api.route("/<string:id>")
def get(id):
    pass


@order_api.route("/", methods=["POST"])
def create():
    payload: dict = request.json
    new_id = create_order(payload)
    return success({
        "id": new_id
    })

@order_api.route("/<string:id>")
def edit(id):
    pass


@order_api.route("/<string:id>")
def delete(id):
    pass
