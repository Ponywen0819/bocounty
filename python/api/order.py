import uuid

from flask import Blueprint, jsonify, request
from utils.auth_util import login_required, get_user_by_token
from utils.order_util import verify_create_form, CreateOrderPayload, ListOrderPayload
from utils.respons_util import make_error_response
from utils.enum_util import APIStatusCode, OrderListCode
from utils import get_now
from database import db
from models import Order, Account, Involve
from datetime import datetime, timedelta, timezone

order_api = Blueprint("order_api", __name__)


@order_api.route("/getOrderList", methods=['GET'])
@login_required
def get_order_list(*args, **kwargs):
    try:
        request_json: dict = request.json
        payload = ListOrderPayload(**request_json)
    except TypeError:
        return make_error_response(APIStatusCode.Wrong_Format, reason='wrong id data type')

    user: Account = get_user_by_token()

    typecode = OrderListCode(payload.type)
    order_list = []
    if typecode == OrderListCode.UsersOrder:
        order_list = Order.query.filter(
            Order.owner_id == user.id
        ).all()
    elif typecode == OrderListCode.InvolveInOrder:
        involve_query = Involve.query.filter(
            Involve.involver_id == user.id
        ).subquery()
        order_list = Order.query.\
            join(involve_query, involve_query.c.order_id == Order.id).all()
    elif typecode == OrderListCode.OpenOrder:
        order_list = Order.query. \
            join(Involve, Involve.order_id == Order.id, isouter=True).\
            filter(
                Involve.involver_id != user.id,
                Order.owner_id != user.id,
                Order.status == 1
            ).all()

    order_info = [
        dict(zip(['id', 'title', 'status'], [row.id, row.title, row.status]))
        for row in order_list
    ]
    return jsonify({
        "status": 0,
        "orders": order_info
    })


@order_api.route('/getOrderInfo', methods=['GET'])
@login_required
def get_order_info(*args, **kwargs):
    try:
        request_json: dict = request.json
        order_id: str = request_json['id']
    except TypeError:
        return make_error_response(APIStatusCode.Wrong_Format, reason='wrong id data type')

    order_info: (Order, str) = db.session.query(Order, Account.name).\
        join(Account, Account.id == Order.owner_id).\
        filter(Order.id == order_id).\
        first()

    if order_info is None:
        return make_error_response(APIStatusCode.RequireMissmatch, reason="request order isn't exist")

    order = order_info[0]

    return jsonify({
        "status": 0,
        "title": order.title,
        "owner_id": order.owner_id,
        "owner_name": order_info[1],
        "start_time": order.start_time,
        "close_time": order.close_time,
        "exec_time": order.exec_time,
        "intro": order.intro
    })


@order_api.route('/changeOrderState', methods=['POST'])
@login_required
def change_order_state(*args, **kwargs):
    pass


@order_api.route('/createOrder', methods=['POST'])
@login_required
@verify_create_form
def create_order(*args, **kwargs):
    request_json: dict = request.json
    payload: CreateOrderPayload = CreateOrderPayload(**request_json)

    user: Account = get_user_by_token()

    if user.bocoin < payload.price:
        return make_error_response(APIStatusCode.CoinNotEnough, reason='coin not enough')

    user.bocoin = user.bocoin - payload.price
    db.session.commit()

    new_id = uuid.uuid4().hex
    new_order = Order(
        id=new_id,
        owner_id=user.id,
        title=payload.title,
        intro=payload.intro,
        price=payload.price,
        close_time=payload.close_time,
        exec_time=payload.exec_time,
        start_time=str(get_now())
    )
    db.session.add(new_order)
    db.session.commit()

    return jsonify({
        "status": 0,
        "id": new_id
    })


@order_api.route('/deleteOrder', methods=['POST'])
@login_required
def del_order():
    order: Order = Order.query.filter(
        Order.id == request.json['id']
    )

    if Order is None:
        return make_error_response(APIStatusCode.RequireMissmatch, reason='no order found')
    else:
        db.session.delete(order)
        db.session.commit()
        return_code = 0
    return jsonify({
        "status": return_code
    })

