from app.database.model.chatroom_member import TABLE, ChatroomMember
from app.database.util import get


def get_chatroom_member_by_id(chatroom_id: str):
    members = get(TABLE, {"chatroom_id": chatroom_id})

    return [ChatroomMember(**data) for data in members]


def get_chatroom_member_by_user_id(account_id: str):
    members = get(TABLE, {"account_id": account_id})

    return [ChatroomMember(**data) for data in members]
