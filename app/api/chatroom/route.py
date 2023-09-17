from flask import Blueprint, request
from app.utils.response import success
from app.utils.auth.auth_util import required_login
from .util.validate import validate_create_payload
from .util.formatter import format_create_payload
from .util.create import create_chatroom, initial_member

chatroom_api = Blueprint("chatroom_api", __name__, url_prefix='/chatroom')


@chatroom_api.route("/", methods=["GET"])
@required_login()
def get_list():
    return success()


@chatroom_api.route("/<string:id>", methods=["POST"])
@required_login()
def creat_chatroom(id):
    validate_create_payload(id)

    format_create_payload(id)

    create_chatroom()
    initial_member()

    return success()
