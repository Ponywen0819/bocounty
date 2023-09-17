from flask import Blueprint, request
from app.utils.response import success
from app.utils.auth.auth_util import required_login
from .util.validate import validate_create_payload
from .util.formatter import format_create_payload
from .util.create import create_report

report_api = Blueprint("repoert_api", __name__, url_prefix='/report')


@report_api.route("/", methods=["GET"])
def get_list():
    return success()


@report_api.route("/<string:id>", methods=["POST"])
@required_login()
def report(id):
    validate_create_payload(id)

    format_create_payload(id)

    create_report()

    return success()
