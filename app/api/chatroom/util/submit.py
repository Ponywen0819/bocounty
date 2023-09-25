from app.database.util import update
from app.database.model.chatroom import (
    ChatroomStatus,
    update_chatroom_by_id
)


def submit_chatroom(chatroom_id: str):
    update_chatroom_by_id(chatroom_id, {
        "status": ChatroomStatus.SUBMIT.value
    })
