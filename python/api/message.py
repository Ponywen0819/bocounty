from flask import Blueprint, request, jsonify
from models import Message, Involve, Order, Account
from utils import get_now
from utils.auth_util import login_required, get_user_by_token
from utils.enum_util import APIStatusCode
from utils.respons_util import make_error_response
from database import db
from sqlalchemy import desc

message_api = Blueprint("message_api", __name__)


@message_api.route('/sendMessage', methods=["POST"])
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

    new_Message = Message(
        chatroom_id=chatroom_id,
        sender_id=user.id,
        content=content,
        time=get_now()
    )

    db.session.add(new_Message)
    db.session.commit()
    return jsonify({
        "status": 0
    })


@message_api.route('/getChatInfo/<id>', methods=["GET"])
@login_required
def get_chat_info(id):
    chatroom_id = id

    chat_room_exist = Involve.query.filter(
        Involve.chatroom_id == chatroom_id
    ).count()

    if chat_room_exist == 0:
        return make_error_response(APIStatusCode.InstanceNotExist, reason="The chatroom with given id isn't exist!")

    involves: Involve = db.session.query(
        Involve.chatroom_id,
        Involve.involver_id,
        Order.owner_id
    ).join(
        Order,
        Order.id == Involve.order_id
    ).filter(
        Involve.chatroom_id == chatroom_id
    ).first()

    chat_info = {
        "status": 0,
        "owner_id": involves[2],
        "chaters": [
            involves[1],
            involves[2]
        ]
    }

    return jsonify(chat_info)


@message_api.route('/getChatHistory/<id>', methods=['GET'])
@login_required
def get_chat_history(id):
    chatroom_id = id

    chat_room_exist = Involve.query.filter(
        Involve.chatroom_id == chatroom_id
    ).count()

    if chat_room_exist == 0:
        return make_error_response(APIStatusCode.InstanceNotExist, reason="The chatroom with given id isn't exist!")

    chatroom_info: Involve = db.session.query(
        Involve.involver_id,
        Order.owner_id
    ).join(
        Order,
        Order.id == Involve.order_id
    ).filter(
        Involve.chatroom_id == chatroom_id
    ).first()

    user: Account = get_user_by_token()

    if (chatroom_info[0] != user.id) and (chatroom_info[1] != user.id):
        return make_error_response(APIStatusCode.InvalidAccess, reason="Access others chatroom!")

    messages = db.session.query(
        Message.raw_id,
        Message.chatroom_id,
        Message.sender_id,
        Message.content,
        Message.time
    ).filter(
        Message.chatroom_id == chatroom_id
    ).order_by(desc(Message.time))

    messages_info = [
        dict(zip(["raw_id", "chatroom_id", "sender_id", "content", "time"], row))
        for row in messages
    ]

    return jsonify({
        "status": 0,
        "list": messages_info
    })


@message_api.route('/assignOrder/<chatroom_id>', methods=["POST"])
@login_required
def assign_order(chatroom_id):
    user: Account = get_user_by_token()

    # verify user is owner of order
    chatroom_info = db.session.query(Involve.involver_id, Order.owner_id, Order.id).join(
        Order,
        Order.id == Involve.order_id
    ).filter(
        Involve.chatroom_id == chatroom_id
    ).first()

    if chatroom_info is None:
        return make_error_response(APIStatusCode.InstanceNotExist, reason="The chatrooom with given id is not exist!")

    if user.id != chatroom_info[1]:
        return make_error_response(APIStatusCode.InvalidAccess, reason="User are not owner of this chatroom!")

    all_involves: list[Involve] = Involve.query.filter(
        Involve.order_id == chatroom_info[2]
    ).all()

    for involve in all_involves:
        print(involve.chatroom_id)
        if involve.chatroom_id != chatroom_id:
            db.session.delete(involve)

    order: Order = Order.query.filter(
        Order.id == chatroom_info[2]
    ).first()

    order.status = 1

    db.session.commit()
    return jsonify({
        "status": 0
    })


@message_api.route('/confirmOrder/<chatroom_id>', methods=["POST"])
@login_required
def confirm_order(chatroom_id):
    user: Account = get_user_by_token()

    # verify user is owner of order
    chatroom_info = db.session.query(Involve.involver_id, Order.owner_id, Order.id).join(
        Order,
        Order.id == Involve.order_id
    ).filter(
        Involve.chatroom_id == chatroom_id
    ).first()

    if chatroom_info is None:
        return make_error_response(APIStatusCode.InstanceNotExist, reason="The chatrooom with given id is not exist!")

    if user.id != chatroom_info[1]:
        return make_error_response(APIStatusCode.InvalidAccess, reason="User are not owner of this chatroom!")

    order: Order = Order.query.filter(
        Order.id == chatroom_info[2]
    ).first()

    involver: Account = Account.query.filter(
        Account.id == chatroom_info[0]
    ).first()

    involver.bocoin += order.price
    order.status = 2

    db.session.commit()
    return jsonify({
        "status": 0
    })
