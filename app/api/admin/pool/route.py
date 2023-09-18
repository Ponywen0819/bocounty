from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.get import get_pool_list

pool_api = Blueprint("pool_admin_api", __name__, url_prefix='/pool')


@pool_api.route("/", methods=["GET"])
@required_login(required_admin=True)
def get_pool_api():
    pools = get_pool_list()

    return success({
        "data": pools
    })
