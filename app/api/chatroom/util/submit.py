from app.database.util import update
from .chatroom import ChatroomStatus

def submit_chatroom(chatroom_id: str):
    update('chatroom', {
        "id": chatroom_id
    }, {
               "status": ChatroomStatus.SUBMIT.value
           })