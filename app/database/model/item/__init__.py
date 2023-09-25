from dataclasses import dataclass
from enum import Enum, auto
from app.database.model import type_checker

TABLE = "item"


class ItemType(Enum):
    CLOTHING = auto()
    EXPRESSION = auto()
    HAIR = auto()
    ACCESSORY = auto()


@dataclass
class Item:
    id: str
    name: str
    photo: str
    type: int

    def __post_init__(self):
        type_checker(self)

        ItemType(self.type)

from .get import *