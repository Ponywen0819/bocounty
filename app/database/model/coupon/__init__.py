from dataclasses import dataclass
from app.database.model import type_checker

TABLE = "coupon"

@dataclass
class Coupon:
    id: str
    type_id: str
    owner_id: str

    def __post_init__(self):
        type_checker(self)

from .get import *
from .create import *