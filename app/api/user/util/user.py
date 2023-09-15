from dataclasses import dataclass


@dataclass
class User:
    id: str
    student_id: str
    name: str
    password: str
    bocoin: int
    intro: str
    verify: str
    role: int
