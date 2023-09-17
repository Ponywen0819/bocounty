from flask import Blueprint, request
from app.utils.response import success
from app.utils.auth.auth_util import required_login
from .util.validate import validate_create_payload, validate_get
from .util.formatter import format_create_payload
from .util.create import create_message
from .util.get import get_messages

message_api = Blueprint("message_api", __name__, url_prefix="/message")


@message_api.route("/<string:id>", methods=["POST"])
@required_login()
def create(id):
    validate_create_payload(id)

    format_create_payload(id)

    create_message()

    return success()


@message_api.route("/<string:id>", methods=["GET"])
def get(id):
    validate_get(id)

    messages = get_messages(id)

    return success({
        "data": messages
    })