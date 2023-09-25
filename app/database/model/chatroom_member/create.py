from app.database.util import create
from app.database.model.chatroom_member import TABLE


def create_member(chatroom_id: str, account_id: str):
    create(TABLE, {
        "chatroom_id": chatroom_id,
        "account_id": account_id
    })
