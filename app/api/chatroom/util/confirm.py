from app.database.model.chatroom import (
    get_chatroom_by_id,
    update_chatroom_by_id,
    ChatroomStatus
)
from app.database.model.order import (
    get_order_by_id,
    update_order_by_id,
    OrderStatus
)
from app.database.model.account import (
    get_account_by_id,
    update_account_by_id
)
from app.database.model.chatroom_member import (
    get_chatroom_member_by_id
)
from app.utils.time_util import get_current_string
from app.utils.auth.auth_util import get_login_user


def confirm_chatroom(chatroom_id: str):
    chatroom = get_chatroom_by_id(chatroom_id)
    order = get_order_by_id(chatroom.order_id)

    update_chatroom_by_id(chatroom_id, {
        "status": ChatroomStatus.CONFIRM.value
    })

    exec_time = get_current_string() if order.exec_time == "None" else order.exec_time
    update_order_by_id(order.id, {
        "status": OrderStatus.COMPLETED.value,
        "exec_time": exec_time
    })

    undertaker_id = get_other_member_id(chatroom_id)
    undertaker = get_account_by_id(undertaker_id)

    update_account_by_id(undertaker.id, {
        "bocoin": undertaker.bocoin + order.price
    })


def get_other_member_id(chatroom_id: str):
    members = get_chatroom_member_by_id(chatroom_id)
    user = get_login_user()

    for member in members:
        member_id = member.account_id
        if member_id != user.get('id'):
            return member_id
