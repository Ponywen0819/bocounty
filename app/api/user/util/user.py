from dataclasses import dataclass, fields


@dataclass
class CreateUser:
    student_id: str
    password: str

    def __post_init__(self):
        type_checker(self)


@dataclass
class EditUser:
    name: str = None
    password: str = None
    intro: str = None

    def __post_init__(self):
        type_checker(self)


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


def type_checker(obj):
    for field in fields(obj):
        instance = getattr(obj, field.name)
        if instance is None:
            continue
        if type(getattr(obj, field.name)) != field.type:
            raise ValueError
