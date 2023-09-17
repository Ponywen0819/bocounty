from app.database.util import get
from .message import Message

def get_messages(id: str):
    messages = get('message',{
        "chatroom_id": id,
    })

    return [Message(**data) for data in messages]