from dataclasses import dataclass
from enum import Enum, auto
from app.database.model import type_checker

TABLE = "pool_item"

@dataclass
class PoolItem:
    pool_id: str
    item_id: str

    def __post_init__(self):
        type_checker(self)


from .get import *
from .update import *
from .delete import *
from .create import *