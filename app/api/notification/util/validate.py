from .notification import ListNotification
from app.database.util import get
from app.utils.response import missing_required, wrong_format, not_found

from flask import request


def validate_list_notification():
    payload: dict = request.json

    try:
        ListNotification(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()

def validate_page():
    payload: dict = request.json

    page = payload.get('page')

    if page < 1:
        wrong_format()


def validate_notification_exist(notification_id: str):
    notification_list = get('notification',{"id": notification_id})

    if len(notification_list) != 1:
        not_found("notification_not found")