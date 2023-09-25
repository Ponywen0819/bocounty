from app.database.model import type_checker
from dataclasses import dataclass
from enum import Enum, auto


class NotificationType(Enum):
    NORMAL = auto()
    ASSIGN = auto()
    CONFIRM = auto()
    REPORT = auto()


@dataclass
class Notification:
    id: str
    type: int
    publisher_id: str
    content: str
    receiver_id: str
    title: str
    timestamp: float

    def __post_init__(self):
        type_checker(self)
