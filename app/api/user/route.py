from flask import Blueprint, request
from app.database.model.account import (
    get_account_by_student_id,
    update_account_by_id
)
from app.utils.response import success
from .util.validate import (
    validate_create_payload,
    validate_edit_payload,
    validate_get,
    validate_name_not_null,
    validate_student_id_not_conflict
)
from app.utils.auth.auth_util import get_login_user
from .util.formatter import format_create_payload, format_edit_payload
from .util.create import create_user
from app.utils.auth.auth_util import required_login

user_api = Blueprint("user_api", __name__, url_prefix="/user")


@user_api.route("/<string:student_id>", methods=["GET"])
@required_login()
def get_detail(student_id):
    validate_get(student_id)

    user = get_account_by_student_id(student_id)

    return success({
        "data": user
    })


@user_api.route("/", methods=["POST"])
def create():
    validate_create_payload()
    validate_student_id_not_conflict()

    format_create_payload()

    create_user()

    return success()


@user_api.route("/", methods=["PUT"])
@required_login()
def edit():
    payload: dict = request.json
    validate_edit_payload()
    validate_name_not_null()

    format_edit_payload()

    user = get_login_user()
    update_account_by_id(user.get('id'), payload)

    return success()
