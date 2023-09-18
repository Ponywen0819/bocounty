from dataclasses import dataclass, fields


@dataclass
class CreateCoupon:
    price: int
    close_time: str
    count: int
    name: str
    describe: str

    def __post_init__(self):
        type_checker(self)


@dataclass
class Coupon:
    price: int
    close_time: str
    count: int
    name: str
    describe: str
    id: str
    publisher_id: str
    start_time: str


def type_checker(obj):
    for field in fields(obj):
        instance = getattr(obj, field.name)
        if instance is None:
            continue
        if type(getattr(obj, field.name)) != field.type:
            raise ValueError
