from app.database.util import get
from app.utils.response import not_found
from .report import Report


def get_report_list():
    reports = get('report')
    return [Report(**data) for data in reports]


def get_report(id: str):
    orders = get('report', {
        "id": id
    })

    if len(orders) != 1:
        not_found("report not found")

    return Report(**orders[0])
