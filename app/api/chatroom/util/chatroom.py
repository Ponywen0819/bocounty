from dataclasses import dataclass
from enum import Enum,auto

class ChatroomStatus(Enum):
    NORMAL = auto()
    SUBMIT = auto()
    CONFIRM = auto()

class OrderStatus(Enum):
    RECRUITING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()

@dataclass
class Chatroom:
    id: str
    order_id: str
    account_id: str


@dataclass
class ChatroomMember:
    chatroom_id: str
    account_id: str
