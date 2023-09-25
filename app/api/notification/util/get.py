from app.database.util import get
from .database import get_notification_with_page

from flask import request
# from .notification import Notification
from app.database.model.notification import Notification

def get_notification(notification_id: str):
    notification = get('notification', {
        "id": notification_id
    })[0]

    return Notification(**notification)


def get_notification_list():
    payload: dict = request.json

    notification_list = get_notification_with_page(**payload)

    return [Notification(**data) for data in notification_list]
