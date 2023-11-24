from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.validate import validate_pool_itme, validate_draw
from .util.get import get_pool_list, get_pool_item
from .util.draw import draw_card

pool_api = Blueprint("pool_api", __name__, url_prefix="/pool")


@pool_api.route("/", methods=["GET"])
@required_login()
def get_pool_api():
    pool_list = get_pool_list()
    return success({
        "data": pool_list
    })


@pool_api.route("/items/<string:pool_id>", methods=["GET"])
@required_login()
def get_pool_items_api(pool_id: str):
    validate_pool_itme(pool_id)

    item_list = get_pool_item(pool_id)

    return success({
        "data": item_list
    })


@pool_api.route("/draw/<string:pool_id>", methods=["POST"])
@required_login()
def draw_api(pool_id: str):
    validate_draw(pool_id)

    item_list = draw_card(pool_id)

    return success({
        "data": item_list
    })


