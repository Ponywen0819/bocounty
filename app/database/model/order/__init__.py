from dataclasses import dataclass
from enum import Enum, auto
from app.database.model import type_checker

TABLE = "order"


class OrderStatus(Enum):
    RECRUITING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()


@dataclass
class Order:
    id: str
    status: int
    title: str
    intro: str
    price: int
    start_time: str
    close_time: str
    exec_time: str
    owner_id: str
    connect_info: str

    def __post_init__(self):
        type_checker(self)

        OrderStatus(self.status)

        if self.price < 1:
            raise ValueError


from .get import *
from .update import *
