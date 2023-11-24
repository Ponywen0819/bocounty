from dataclasses import dataclass
from enum import Enum, auto


class DrawType(Enum):
    single = auto()
    multi = auto()


@dataclass
class Pool:
    id: str
    name: str
    photo: str
    close_time: str
    start_time: str


@dataclass
class PoolItem:
    pool_id: str
    item_id: str
