from dataclasses import dataclass
from app.database.model import type_checker


@dataclass
class LoginPayload:
    student_id: str
    password: str

    def __post_init__(self):
        type_checker(self)
