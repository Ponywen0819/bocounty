from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.validate import (
    validate_create_payload,
    validate_name,
    validate_type,
    validate_photo
)

from .util.formatter import (
    format_create_payload
)

from .util.create import create_item, save_photo
from app.database.model.item import get_item_list

item_api = Blueprint("admin_item_api", __name__, url_prefix="/item")


@item_api.route("/", methods=["GET"])
@required_login(required_admin=True)
def list_item_api():
    item_list = get_item_list()

    return success({"data": item_list})


@item_api.route("/", methods=["POST"])
@required_login(required_admin=True)
def create_item_api():
    validate_create_payload()
    validate_name()
    validate_type()
    validate_photo()

    format_create_payload()

    save_photo()
    create_item()

    return success()
