from app.database.model import type_checker
from dataclasses import dataclass
from enum import Enum, auto

TABLE = 'chatroom'


class ChatroomStatus(Enum):
    RECRUITING = auto()
    NORMAL = auto()
    SUBMIT = auto()
    CONFIRM = auto()


@dataclass
class Chatroom:
    id: str
    order_id: str
    status: int

    def __post_init__(self):
        type_checker(self)


from .get import *
from .update import *
from .create import *