from flask import current_app, Blueprint
from utils.auth_util import require_login

item_api = Blueprint("item_api", __name__)


@item_api.route('/getPoolItemList', methods=['GET'])
@require_login
def get_pool_list(*args, **kwargs):
    pass


@item_api.route('/drawCards', methods=['POST'])
@require_login
def drae_cards(*args, **kwargs):
    pass
