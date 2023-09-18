from dataclasses import dataclass, fields
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

    def __post_init__(self):
        type_checker(self)


def type_checker(obj):
    for field in fields(obj):
        instance = getattr(obj, field.name)
        if instance is None:
            continue
        if type(getattr(obj, field.name)) != field.type:
            raise ValueError
