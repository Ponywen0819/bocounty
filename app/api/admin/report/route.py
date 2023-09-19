from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.validate import (
    validate_report_exist
)
from .util.get import get_report_list, get_report

report_api = Blueprint("report_admin_api", __name__, url_prefix='/report')


@report_api.route("/", methods=["GET"])
@required_login(required_admin=True)
def get_report_list_api():
    report_list = get_report_list()

    return success({
        "data": report_list
    })


@report_api.route("/<string:report_id>", methods=["GET"])
@required_login(required_admin=True)
def get_report_api(report_id: str):
    validate_report_exist(report_id)

    report = get_report(report_id)

    return success({
        "data": report
    })
