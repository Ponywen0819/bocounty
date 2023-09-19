from flask import Blueprint
from app.utils.auth.auth_util import required_login
from app.utils.response import success

from .util.get import get_report_list

report_api = Blueprint("report_admin_api", __name__, url_prefix='/report')


@report_api.route("/", methods=["GET"])
@required_login(required_admin=True)
def get_report_list_api():

    report_list = get_report_list()

    return success({
        "data": report_list
    })