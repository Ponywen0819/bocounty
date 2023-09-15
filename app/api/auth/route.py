from flask import Blueprint, request
from app.utils.respons_util import success
from .util import get_user
from app.api.user.route import create
from .util.response import with_jwt, without_jwt

auth_api = Blueprint("auth_api", __name__, url_prefix='/auth')


@auth_api.route("/login", methods=["POST"])
def login():
    payload: dict = request.json
    user = get_user(payload)

    return with_jwt(success(), user)


@auth_api.route("/logout", methods=["POST"])
def register():
    return without_jwt(success())
