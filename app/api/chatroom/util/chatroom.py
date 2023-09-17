from dataclasses import dataclass


@dataclass
class Chatroom:
    id: str
    order_id: str
    account_id: str


@dataclass
class ChatroomMember:
    chatroom_id: str
    account_id: str
