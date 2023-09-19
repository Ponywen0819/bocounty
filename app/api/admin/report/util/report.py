from dataclasses import dataclass

@dataclass
class Report:
    id: str
    order_id: str
    type: int
    publisher_id: str
    time: str