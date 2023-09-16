from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CreatePayload:
    title: str
    intro: str
    price: int
    close_time = str


@dataclass
class Order:
    id: str
    status: int
    title: str
    intro: str
    price: int
    owner_id: str
    start_time: datetime
    close_time: datetime
    exec_time: datetime = None

