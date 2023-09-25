from app.database.util import get
from app.utils.auth.auth_util import get_login_user


def send_notification(request_id: str):
    request = get('request', {"id": request_id})[0]


def send_delete_confirm(request_id: str):
    request = get('request', {"id": request_id})[0]

    send_message(f"""""")

def send_been_delete(request_id: str):
    request = get('request', {"id": request_id})[0]


def send_message(content: str, title: str, publisher_id: str, receiver_id: str):
    pass