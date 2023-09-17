from dataclasses import dataclass
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


