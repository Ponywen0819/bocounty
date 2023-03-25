import uuid

from flask import Blueprint, jsonify
from utils.auth_util import login_required
from utils.order_util import verify_create_form, CreateOrderPayload
from database import db
from models import Order, Account
from datetime import datetime, timedelta, timezone

order_api = Blueprint("order_api", __name__)


@order_api.route("/getOrderList", methods=['GET'])
@login_required
def get_order_list(*args, **kwargs):
    pass


@order_api.route('/getOrderInfo', methods=['GET'])
@login_required
def get_order_info(*args, **kwargs):
    pass


@order_api.route('/changeOrderState', methods=['POST'])
@login_required
def change_order_state(*args, **kwargs):
    pass


@order_api.route('/createOrder', methods=['POST'])
@login_required
@verify_create_form
def create_order(*args, **kwargs):
    payload: CreateOrderPayload = kwargs['payload']
    user: Account = kwargs['user']
    new_id = uuid.uuid4().hex
    tz = timezone(timedelta(hours=+8))
    new_order = Order(
        id=new_id,
        ownser_id=user.id,
        title=payload.title,
        intro=payload.intro,
        price=payload.price,
        close_time=payload.close_time,
        exec_time=payload.exec_time,
        start_time=str(datetime.now(tz))
    )
    db.session.add(new_order)
    db.session.commit()

    return jsonify({
        "status": 0,
        "id": new_id
    })


@order_api.route('/deleteOrder', methods=['POST'])
def del_order():
    pass
