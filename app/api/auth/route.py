from flask import Blueprint
from .util.cookie import with_jwt, without_jwt
from app.utils.response import success
from app.utils.auth.auth_util import get_jwt_data, get_login_user
from .util.validate import (
    validate_password_correct,
    validate_verify_status,
    validate_login_payload
)

auth_api = Blueprint("auth_api", __name__, url_prefix='/auth')


@auth_api.route("/login", methods=["POST"])
def login():
    validate_login_payload()
    user = validate_password_correct()
    validate_verify_status(user)

    return with_jwt(success(), user)


@auth_api.route("/logout", methods=["POST"])
def register():
    return without_jwt(success())


@auth_api.route("/verify", methods=["POST"])
def verify():
    data = get_jwt_data()
    user = get_login_user()
    return with_jwt(success({
        "data": data
    }), user)
