from flask import Blueprint, jsonify, request
from app.utils.response import success
from .util import get_user_list, get_user, create_user, delete_user
from app.utils.auth.auth_util import required_login

user_api = Blueprint("user_api", __name__, url_prefix="/user")


@user_api.route("/", methods=["GET"])
@required_login(required_admin=True)
def get_list():
    users = get_user_list()
    return success({
        "users": jsonify(users)
    })


@user_api.route("/<string:id>", methods=["GET"])
@required_login()
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
@required_login()
def edit(id):
    payload: dict = request.json


@user_api.route("/<string:id>", methods=["DELETE"])
@required_login(required_admin=True)
def delete(id):
    get_user(id)
    delete_user(id)

    return success()
