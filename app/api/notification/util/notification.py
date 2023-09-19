from dataclasses import dataclass

from app.utils.payload import type_checker


@dataclass
class ListNotification:
    page: int

    def __post_init__(self):
        type_checker(self)


@dataclass
class Notification:
    id: str
    publisher_id: str
    receiver_id: str
    content: str
    title: str
    timestamp: float

    def __post_init__(self):
        type_checker(self)
