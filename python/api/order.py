from flask import Blueprint
from utils.auth_util import require_login

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
def create_order():
    pass


@order_api.route('/deleteOrder', methods=['POST'])
def del_order():
    pass
