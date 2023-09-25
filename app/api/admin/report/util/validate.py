from app.utils.response import not_found
from app.database.util import get


def validate_report_exist(report_id: str):
    report_list = get('report', {"id": report_id})

    if len(report_list) != 1:
        not_found('report not found')
