from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CreatePayload:
    title: str
    intro: str
    price: int
    close_time = str
    exec_time: datetime = None


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

    def __post_init__(self):
        self.close_time = datetime.fromisoformat(self.close_time)
