from app.database.model.chatroom_member import (
    create_member
)
from app.database.model.order import get_order_by_id
from app.utils.auth.auth_util import get_login_user


def initial_member(payload: dict):
    order_id = payload.get('order_id')

    order = get_order_by_id(order_id)

    create_member(
        chatroom_id=payload.get('id'),
        account_id=order.owner_id
    )

    user = get_login_user()
    create_member(
        chatroom_id=payload.get('id'),
        account_id=user.get('id')
    )
