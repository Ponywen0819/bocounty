from flask import Blueprint
from utils.auth_util import login_required

message_api = Blueprint("message_api", __name__)


@message_api.route('/sendMessage', methods=['POSt'])
def send_message():
    pass


@message_api.route('/getChatInfo', methods=['GET'])
@login_required
def get_chat_info(*args, **kwargs):
    pass


@message_api.route('/getChatHistory', methods=['GET'])
@login_required
def get_chat_history(*args, **kwargs):
    pass


@message_api.route('/assignOrder', methods=['POST'])
@login_required
def assign_order(*args, **kwargs):
    pass


@message_api.route('/confirmOrder', methods=['POST'])
@login_required
def confirm_order(*args, **kwargs):
    pass
