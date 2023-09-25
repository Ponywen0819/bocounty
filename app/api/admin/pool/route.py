from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success
from app.database.model.pool_item import get_pool_item, delete_by_id, create_pool_item

from .util.validate import (
    validate_create_payload,
    validate_update_payload,
    validate_name,
    validate_photo,
    validate_close_time,
    validate_pool_exist,
    validate_item_in_pool,
    validate_item_not_in_pool,
validate_item_exist
)
from .util.formatter import format_create_payload
from .util.get import get_pool_list
from .util.create import save_photo, create_pool
from .util.delete import delete_pool
from .util.edit import edit_pool

pool_api = Blueprint("pool_admin_api", __name__, url_prefix='/pool')


@pool_api.route("/", methods=["GET"])
@required_login(required_admin=True)
def get_pool_api():
    pools = get_pool_list()

    return success({
        "data": pools
    })


@pool_api.route("/", methods=["POST"])
@required_login(required_admin=True)
def create_pool_api():
    validate_create_payload()
    validate_photo()
    validate_name()
    validate_close_time()

    format_create_payload()

    save_photo()
    create_pool()

    return success()


@pool_api.route("/<string:pool_id>", methods=["PUT"])
@required_login(required_admin=True)
def edit_pool_api(pool_id: str):
    validate_update_payload()
    validate_name()
    validate_close_time()
    validate_photo()
    validate_pool_exist(pool_id)

    save_photo()
    edit_pool(pool_id)

    return success()


@pool_api.route("/<string:pool_id>", methods=["DELETE"])
@required_login(required_admin=True)
def delete_pool_api(pool_id: str):
    validate_pool_exist(pool_id)

    delete_pool(pool_id)

    return success()


@pool_api.route("/<string:pool_id>/item", methods=["GET"])
@required_login(required_admin=True)
def get_pool_item_api(pool_id: str):
    validate_pool_exist(pool_id)

    item_list = get_pool_item(pool_id)

    return success({"data": item_list})


@pool_api.route("/<string:pool_id>/item/<string:item_id>", methods=["POST"])
@required_login(required_admin=True)
def edit_pool_item_api(pool_id: str, item_id: str):
    validate_pool_exist(pool_id)
    validate_item_exist(item_id)
    validate_item_not_in_pool(pool_id, item_id)

    create_pool_item(pool_id, item_id)

    return success()


@pool_api.route("/<string:pool_id>/item/<string:item_id>", methods=["DELETE"])
@required_login(required_admin=True)
def delete_pool_item_api(pool_id: str, item_id: str):
    validate_pool_exist(pool_id)
    validate_item_in_pool(pool_id, item_id)

    delete_by_id(pool_id, item_id)

    return success()
