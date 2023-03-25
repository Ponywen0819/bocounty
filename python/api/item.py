from flask import current_app, Blueprint
from utils.auth_util import login_required

item_api = Blueprint("item_api", __name__)


@item_api.route('/getPoolItemList', methods=['GET'])
@login_required
def get_pool_list(*args, **kwargs):
    pass


@item_api.route('/drawCards', methods=['POST'])
@login_required
def drae_cards(*args, **kwargs):
    pass
