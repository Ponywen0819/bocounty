from flask import Blueprint
from app.utils.response import success
from app.utils.auth.auth_util import required_login
from .util.validate import validate_create_payload, validate_assign
from .util.formatter import format_create_payload
from .util.get import get_chatroom_list
from .util.create import create_chatroom, initial_member
from .util.assign import assign_order

chatroom_api = Blueprint("chatroom_api", __name__, url_prefix='/chatroom')


@chatroom_api.route("/", methods=["GET"])
@required_login()
def get_list():
    chatroom_list = get_chatroom_list()

    return success({
        "data": chatroom_list
    })


@chatroom_api.route("/<string:order_id>", methods=["POST"])
@required_login()
def creat_chatroom(order_id):
    validate_create_payload(order_id)

    format_create_payload(order_id)

    create_chatroom()
    initial_member()

    return success()


@chatroom_api.route("/assign/<string:chatroom_id>", methods=["POST"])
def assign_chatroom(chatroom_id: str):
    validate_assign(chatroom_id)

    assign_order(chatroom_id)

    return success()
