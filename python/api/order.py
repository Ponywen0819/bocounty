from flask import Blueprint, request
from utils.auth_util import require_login
from utils.order_util import verify_create_form

order_api = Blueprint("order_api", __name__)


@order_api.route("/getOrderList", methods=['GET'])
@require_login
def get_order_list(*args, **kwargs):
    pass


@order_api.route('/getOrderInfo', methods=['GET'])
@require_login
def get_order_info(*args, **kwargs):
    pass


@order_api.route('/changeOrderState', methods=['POST'])
@require_login
def change_order_state(*args, **kwargs):
    pass


@order_api.route('/createOrder', methods=['POST'])
@require_login
@verify_create_form
def create_order():
    req_json: dict = request.json



@order_api.route('/deleteOrder', methods=['POST'])
def del_order():
    pass
