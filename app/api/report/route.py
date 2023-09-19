from flask import Blueprint
from app.utils.response import success
from app.utils.auth.auth_util import required_login
from .util.validate import validate_create_payload, validate_not_reported
from .util.formatter import format_create_payload
from .util.create import create_report

report_api = Blueprint("report_api", __name__, url_prefix='/report')


@report_api.route("/<string:order_id>", methods=["POST"])
@required_login()
def report(order_id):
    validate_create_payload(order_id)
    validate_not_reported(order_id)

    format_create_payload(order_id)

    create_report()

    return success()
