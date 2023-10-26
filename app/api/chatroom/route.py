from flask import Blueprint
from app.utils.response import success
from app.database.model.chatroom import (
    get_user_chatroom_list,
    create_chatroom
)
from app.database.model.chatroom_member import (
    get_chatroom_member_by_id
)
from app.database.model.account import (
    get_account_by_member_record
)
from app.utils.auth.auth_util import required_login
from .util.validate import (
    validate_create_payload,
    validate_assign,
    validate_member,
    validate_chatroom_exist,
    validate_is_owner,
    validate_not_owner,
    validate_is_member,
    validate_not_submit,
    validate_not_finish,
    validate_not_recruiting
)

from .util.initial import initial_member
from .util.formatter import format_create_payload
from .util.assign import assign_order
from .util.submit import submit_chatroom
from .util.notification import send_submit_message, send_confirm_message
from .util.confirm import confirm_chatroom

chatroom_api = Blueprint("chatroom_api", __name__, url_prefix='/chatroom')


@chatroom_api.route("/", methods=["GET"])
@required_login()
def get_list():
    chatroom_list = get_user_chatroom_list()

    return success({
        "data": chatroom_list
    })


@chatroom_api.route("/<string:order_id>", methods=["POST"])
@required_login()
def creat_chatroom(order_id):
    validate_create_payload(order_id)

    payload = format_create_payload(order_id)

    create_chatroom(payload)
    initial_member(payload)

    return success()


@chatroom_api.route("/member/<string:chatroom_id>", methods=["GET"])
@required_login()
def get_chatroom_member_api(chatroom_id: str):
    validate_member(chatroom_id)

    member_records = get_chatroom_member_by_id(chatroom_id)
    accounts = get_account_by_member_record(member_records)

    return success({
        "data": accounts
    })


@chatroom_api.route("/assign/<string:chatroom_id>", methods=["POST"])
@required_login()
def assign_chatroom(chatroom_id: str):
    validate_assign(chatroom_id)
    validate_not_recruiting(chatroom_id)

    assign_order(chatroom_id)

    return success()


# @chatroom_api.route("/submit/<string:chatroom_id>", methods=["POST"])
# @required_login()
# def submit_chatroom_api(chatroom_id: str):
#     validate_chatroom_exist(chatroom_id)
#     validate_is_member(chatroom_id)
#     validate_not_owner(chatroom_id)
#     validate_not_submit(chatroom_id)
#
#     submit_chatroom(chatroom_id)
#     send_submit_message(chatroom_id)
#
#     return success()


@chatroom_api.route("/confirm/<string:chatroom_id>", methods=["POST"])
@required_login()
def confire_chatroom_api(chatroom_id: str):
    validate_chatroom_exist(chatroom_id)
    validate_is_member(chatroom_id)
    validate_is_owner(chatroom_id)
    validate_not_finish(chatroom_id)

    confirm_chatroom(chatroom_id)
    send_confirm_message(chatroom_id)

    return success()
