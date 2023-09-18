from dataclasses import dataclass
from enum import Enum, auto


class Type(Enum):
    CLOTHING = auto()
    EXPRESSION = auto()
    HAIR = auto()
    ACCESSORY = auto()


@dataclass
class CreateItem:
    name: str
    photo: str
    type: int
