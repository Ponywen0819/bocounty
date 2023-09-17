from flask import Blueprint, jsonify, request
from app.utils.response import success
from .util.validate import validate_create_payload, validate_edit_payload, validate_get
from .util.formatter import format_create_payload, format_edit_payload
from .util.get import get_user
from .util.create import create_user
from .util.edit import edit_user
from app.utils.auth.auth_util import required_login

user_api = Blueprint("user_api", __name__, url_prefix="/user")


@user_api.route("/<string:student_id>", methods=["GET"])
@required_login()
def get_detail(student_id):
    validate_get(student_id)

    user = get_user(student_id)

    return success({
        "data": user
    })


@user_api.route("/", methods=["POST"])
def create():
    validate_create_payload()

    format_create_payload()

    create_user()

    return success()


@user_api.route("/<string:student_id>", methods=["PUT"])
@required_login()
def edit(student_id: str):
    validate_edit_payload(student_id)

    format_edit_payload()

    edit_user()

    return success()

