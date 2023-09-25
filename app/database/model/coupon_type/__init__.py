from dataclasses import dataclass
from app.database.model import type_checker

@dataclass
class CreateCouponType:
    price: int
    close_time: str
    count: int
    name: str
    describe: str

    def __post_init__(self):
        type_checker(self)


@dataclass
class CouponType:
    id: str
    price: int
    publisher_id: str
    start_time: str
    close_time: str
    describe: str
    count: int
    name: str

    def __post_init__(self):
        type_checker(self)
