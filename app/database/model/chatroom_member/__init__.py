from dataclasses import dataclass
from app.database.model import type_checker

TABLE = 'chatroom_member'


@dataclass
class ChatroomMember:
    chatroom_id: str
    account_id: str

    def __post_init__(self):
        type_checker(self)

from .get import *
from .create import *