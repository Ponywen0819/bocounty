from flask import Blueprint, request
from .util.cookie import with_jwt, without_jwt
from app.utils.response import success
from app.utils.auth.auth_util import get_jwt_data, get_login_user
from .util import get_user

auth_api = Blueprint("auth_api", __name__, url_prefix='/auth')


@auth_api.route("/login", methods=["POST"])
def login():
    payload: dict = request.json
    user = get_user(payload)

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
