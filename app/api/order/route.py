from flask import Blueprint

order_api = Blueprint("order_api", __name__, url_prefix="/order")


@order_api.route("/", methods=["GET"])
def list():
    pass


@order_api.route("/<string:id>")
def get(id):
    pass


@order_api.route("/")
def create():
    pass


@order_api.route("/<string:id>")
def edit(id):
    pass


@order_api.route("/<string:id>")
def delete(id):
    pass
