from dataclasses import dataclass
from app.database.model import type_checker

@dataclass
class CreateMessage:
    content: str

    def __post_init__(self):
        type_checker(self)

        while len(self.content) > 0:
            if self.content[0] == " ":
                self.content = self.content[1:]

            else:
                break

        if self.content == "":
            raise ValueError

@dataclass
class Message:
    id: str
    chatroom_id: str
    sender_id: str
    content: str
    time: str
    timestamp: float

    def __post_init__(self):
        type_checker(self)