from app.database.util import create, get
from app.utils.auth.auth_util import get_login_user
from app.database.model.notification import NotificationType
from uuid import uuid4
from datetime import datetime
from time import time


def send_submit_message(chatroom_id: str):
    user = get_login_user()

    chatroom = get('chatroom', {"id": chatroom_id})[0]
    order = get('order', {"id": chatroom.get('order_id')})[0]

    send_message(
        f"""懸賞主題：<【{order.get('title')}】> 懸賞編號： <{order.get('id')}>\n<{user.get('name')}> 已完成任務，若確認委託完成，請按下【完成】按鈕，我們隨後將會撥款 <{order.get('price')} Bocoin> 到對方的帳號中!""",
        user.get('id'),
        "冒險者完成委託囉!\n請確認結果並標示完成。",
        order.get('owner_id'),
        NotificationType.REPORT
    )


def send_confirm_message(chatroom_id: str):
    user = get_login_user()

    chatroom = get('chatroom', {"id": chatroom_id})[0]
    order = get('order', {"id": chatroom.get('order_id')})[0]

    send_message(
        f"""懸賞主題：<【{order.get('title')}】> 懸賞編號： <{order.get('id')}>\n<{user.get('name')}> 已確認您的交付結果，系統已將 <{order.get('price')} Bocoin> 發派到您的帳戶中，請至冒險者檔案中確認。""",
        user.get('id'),
        "委託成立囉!已將報酬加入您的帳戶中! ",
        get_other_member(chatroom_id),
        NotificationType.CONFIRM
    )


def send_message(content: str, publisher_id: str, title: str, receiver_id: str, type: NotificationType):
    new_id = uuid4().hex

    create('notification', {
        "id": new_id,
        "content": content,
        "publisher_id": publisher_id,
        "receiver_id": receiver_id,
        "title": title,
        "timestamp": time(),
        "type": type.value
    })


def get_other_member(chatroom_id: str):
    chatroom_members = get('chatroom_member', {"chatroom_id": chatroom_id})
    user = get_login_user()

    for chatroom_member in chatroom_members:
        member_id = chatroom_member.get('account_id')
        if member_id != user.get('id'):
            return member_id
