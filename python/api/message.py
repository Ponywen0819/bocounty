from flask import Blueprint
from utils.auth_util import require_login

message_api = Blueprint("message_api", __name__)


@message_api.route('/getChatInfo', methods=['GET'])
@require_login
def get_chat_info(*args, **kwargs):
    pass


@message_api.route('/getChatHistory', methods=['GET'])
@require_login
def get_chat_histort(*args, **kwargs):
    pass


@message_api.route('/assignOrder', methods=['POST'])
@require_login
def assign_order(*args, **kwargs):
    pass


@message_api.route('/confirmOrder', methods=['POST'])
@require_login
def confirm_order(*args, **kwargs):
    pass
