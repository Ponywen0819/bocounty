from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.validate import (
    validate_get_wear,
    validate_update_wear,
    validate_item_exist
)
from .util.get import get_user_wearing
from .util.update import update_wear

item_api = Blueprint("item_api", __name__, url_prefix='/item')


@item_api.route("/wear/<string:student_id>", methods=["GET"])
@required_login()
def get_user_wearing_api(student_id: str):
    validate_get_wear(student_id)

    items = get_user_wearing(student_id)

    return success({
        "data": items
    })


@item_api.route("/wear", methods=["PUT"])
@required_login()
def change_user_wearing_api():
    validate_update_wear()
    validate_item_exist()

    update_wear()

    return success()


@item_api.route("/own/<string:student_id>")
@required_login()
def get_user_own_api(student_id: str):
    return success()
