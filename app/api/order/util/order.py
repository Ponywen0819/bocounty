from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    id: str
    status: int
    title: str
    intro: str
    price: int
    start_time: datetime
    close_time: datetime
    exec_time: datetime
    owner_id: str
