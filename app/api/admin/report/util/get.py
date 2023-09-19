from app.database.util import get
from .report import Report


def get_report_list():
    report_list = get('report')

    return [Report(**data) for data in report_list]
