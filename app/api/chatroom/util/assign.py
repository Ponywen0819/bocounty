from app.database.util import get, update, get_db
from .chatroom import OrderStatus
from app.database.model.chatroom import (
    get_chatroom_by_id,
    update_chatroom_by_id,
    ChatroomStatus
)
from app.database.model.order import update_order_by_id


def assign_order(chatroom_id: str):
    chatroom = get_chatroom_by_id(chatroom_id)

    update_order_by_id(chatroom.order_id, {
        "status": OrderStatus.IN_PROGRESS.value
    })

    remove_recruiting_chatroom(chatroom_id, chatroom.order_id)
    update_chatroom_to_normal(chatroom_id)


def remove_recruiting_chatroom(chatroom_id: str, order_id: str):
    cursor = get_db().cursor()
    cursor.execute(f"""
        DELETE FROM 'chatroom'
        WHERE id != '{chatroom_id}' AND order_id = '{order_id}'
    """)


def update_chatroom_to_normal(chatroom_id: str):
    update_chatroom_by_id(chatroom_id, {
        "status": ChatroomStatus.NORMAL.value
    })
