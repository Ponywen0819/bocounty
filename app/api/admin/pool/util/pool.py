from dataclasses import dataclass, fields


@dataclass
class CreatePool:
    name: str
    photo: str
    close_time: str = None

    def __post_init__(self):
        type_checker(self)


@dataclass
class Pool:
    id: str
    name: str
    photo: str
    start_time: str
    close_time: str

    def __post_init__(self):
        type_checker(self)


def type_checker(obj):
    for field in fields(obj):
        instance = getattr(obj, field.name)
        if instance is None:
            continue
        if type(getattr(obj, field.name)) != field.type:
            raise ValueError
