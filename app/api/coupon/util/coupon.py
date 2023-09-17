from dataclasses import dataclass


@dataclass
class Coupon:
    id: str
    owner_id: str
    close_time: str
    describe: str
    name: str
    count: int


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
