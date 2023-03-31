from flask import Blueprint, request, jsonify
from models import Message, Involve, Order, Account
from utils.auth_util import login_required, get_user_by_token
from utils.enum_util import APIStatusCode
from utils.respons_util import make_error_response
from database import db
from sqlalchemy import desc

message_api = Blueprint("message_api", __name__)


@message_api.route('/sendMessage', methods=['POST'])
@login_required
def send_message():
    request_json: dict = request.json
    if "chatroom_id" not in request_json.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason="missing 'chatroom_id' argument!")
    chatroom_id = request_json["chatroom_id"]

    if "content" not in request_json.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason="missing 'content' argument!")
    content = request_json["content"]

    # verify chatroom exist
    involvers = db.session.query(Involve.involver_id, Order.owner_id).join(
        Order,
        Order.id == Involve.order_id
    ).filter(
        Involve.chatroom_id == chatroom_id
    ).first()

    if involvers is None:
        return make_error_response(APIStatusCode.InstanceNotExist, reason="The chatroom with given id is not exist!")

    # verify user is valid user in given chatroom
    user: Account = get_user_by_token()
    if (user.id != involvers[0]) and (user.id != involvers[1]):
        return make_error_response(APIStatusCode.InvalidAccess, reason="invalid access!")


@message_api.route('/getChatInfo', methods=['GET'])
@login_required
def get_chat_info(*args, **kwargs):
    chat_id = request.args.get("id", None)
    if chat_id is None:
        return make_error_response(APIStatusCode.Wrong_Format, reason="missing 'id' arguments!")

    chat_room_exist = Involve.query.filter(
        Involve.chatroom_id == chat_id
    ).exists()

    if not chat_room_exist:
        return make_error_response(APIStatusCode.InstanceNotExist, reason="The chatroom with given id isn't exist!")

    involves: Involve = db.session.query(
        Involve.chatroom_id,
        Involve.involver_id,
        Order.owner_id
    ).join(
        Order,
        Order.id == Involve.order_id
    ).filter(
        Involve.chatroom_id == chat_id
    ).first();

    chat_info = {
        "status": 0,
        "owner_id": involves[2],
        "chaters": [
            involves[1],
            involves[2]
        ]
    }

    return jsonify(chat_info)


@message_api.route('/getChatHistory', methods=['GET'])
@login_required
def get_chat_history(*args, **kwargs):
    chat_id = request.args.get("id", None)

    if chat_id is None:
        return make_error_response(APIStatusCode.Wrong_Format, reason="missing 'id' arguments!")

    chat_room_exist = Involve.query.filter(
        Involve.chatroom_id == chat_id
    ).exists()

    if not chat_room_exist:
        return make_error_response(APIStatusCode.InstanceNotExist, reason="The chatroom with given id isn't exist!")

    messages = db.session.query(
        Message.chatroom_id,
        Message.sender_id,
        Message.content,
        Message.time
    ).filter(
        Message.chatroom_id == chat_id
    ).order_by(desc(Message.time))

    messages_info = [
        zip(["chatroom_id", "sender_id", "content", "time"], row)
        for row in messages
    ]

    return jsonify({
        "status": 0,
        "list": messages_info
    })


@message_api.route('/assignOrder', methods=['POST'])
@login_required
def assign_order(*args, **kwargs):
    pass


@message_api.route('/confirmOrder', methods=['POST'])
@login_required
def confirm_order(*args, **kwargs):
    pass
