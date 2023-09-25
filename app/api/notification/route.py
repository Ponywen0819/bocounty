from app.utils.auth.auth_util import required_login
from app.utils.response import success

from flask import Blueprint

from .util.validate import (
    validate_list_notification,
    validate_page,
    validate_notification_exist
)
from .util.get import (
    get_notification,
    get_notification_list,
)

notification_api = Blueprint("notification_api", __name__, url_prefix='/notification')


@notification_api.route("/", methods=['GET'])
@required_login()
def get_notification_list_api():
    validate_list_notification()
    validate_page()

    notification_list = get_notification_list()

    return success({
        "data": notification_list
    })


@notification_api.route("/<string:notification_id>", methods=['GET'])
@required_login()
def get_notification_api(notification_id: str):
    validate_notification_exist(notification_id)

    notification = get_notification(notification_id)

    return success({
        "data": notification
    })
