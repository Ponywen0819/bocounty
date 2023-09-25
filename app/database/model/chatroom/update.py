from app.database.util import update
from app.database.model.chatroom import TABLE


def update_chatroom_by_id(chatroom_id: str, values: dict):
    update(TABLE, {"id": chatroom_id}, values)
