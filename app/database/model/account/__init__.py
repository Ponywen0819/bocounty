from app.database.model import type_checker
from dataclasses import dataclass

TABLE = "account"

@dataclass
class Account:
    id: str
    student_id: str
    name: str
    password: str
    bocoin: int
    intro: str
    verify: int
    role: int

    def __post_init__(self):
        type_checker(self)


from .get import *
from .update import *