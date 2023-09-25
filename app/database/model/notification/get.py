from app.database.util import get
from ..notification import Notification


def gat_notification_by_id(notification_id):
    notification_list = get('notification', {"id": notification_id})
    return [Notification(**data) for data in notification_list]
