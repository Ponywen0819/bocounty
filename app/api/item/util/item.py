from dataclasses import dataclass


@dataclass
class Item:
    id: str
    name: str
    photo: str
    type: int
