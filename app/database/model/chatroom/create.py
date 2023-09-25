from app.database.util import create
from app.database.model.chatroom import TABLE


def create_chatroom(payload):
    create(TABLE, payload)
