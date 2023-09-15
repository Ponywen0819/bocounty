from flask import Blueprint, jsonify, request
from app.utils.respons_util import success
from .util import get_user_list, get_user, create_user, delete_user

user_api = Blueprint("user_api", __name__, url_prefix="/user")


@user_api.route("/", methods=["GET"])
def get_list():
    users = get_user_list()
    return jsonify(users)


@user_api.route("/<string:id>", methods=["GET"])
def get_detail(id):
    user = get_user(id)
    return jsonify(user)


@user_api.route("/", methods=["POST"])
def create():
    payload: dict = request.json
    user_id = create_user(payload)

    return success({
        "id": user_id
    })


@user_api.route("/<string:id>", methods=["PUT"])
def edit(id):
    payload: dict = request.json


@user_api.route("/<string:id>", methods=["DELETE"])
def delete(id):
    get_user(id)
    delete_user(id)

    return success()
