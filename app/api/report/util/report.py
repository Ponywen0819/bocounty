from dataclasses import dataclass, fields
from enum import Enum, auto


class Type(Enum):
    MISLEADING_OR_FRAUD = 1
    PORNOGRAPHIC_CONTENT = 2
    HARASSMENT = 3
    SPAM = 4
    OTHER = 5


@dataclass
class CreateReport:
    type: int

    def __post_init__(self):
        type_checker(self)


@dataclass
class Report:
    id: str
    type: int
    order_id: str
    publisher_id: str
    time: str

def type_checker(obj):
    for field in fields(obj):
        instance = getattr(obj, field.name)
        if instance is None:
            continue
        if type(getattr(obj, field.name)) != field.type:
            raise ValueError
