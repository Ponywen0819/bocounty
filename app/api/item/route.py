from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.validate import validate_get_wear, validate_update_wear
from .util.get import get_user_wearing

item_api = Blueprint("item_api", __name__, url_prefix='/item')


@item_api.route("/wear/<string:student_id>", methods=["GET"])
@required_login()
def get_user_wearing_api(student_id: str):
    validate_get_wear(student_id)

    items = get_user_wearing(student_id)

    return success({
        "data": items
    })


@item_api.route("/wear/<string:student_id>", methods=["PUT"])
@required_login()
def change_user_wearing_api(student_id: str):
    validate_update_wear(student_id)

    return success()


@item_api.route("/own/<string:student_id>")
@required_login()
def get_user_own_api(student_id: str):
    return success()
