from app.database.util import get
from .report import Report


def get_report_list():
    reports = get('report')
    return [Report(**data) for data in reports]
