from dataclasses import dataclass, fields

@dataclass
class CreatePayload:
    title: str
    intro: str
    price: int
    connect_info: str
    close_time: str
    exec_time: str

    def __post_init__(self):
        type_checker(self)


@dataclass
class UpdatePayload:
    title: str
    intro: str
    close_time: str
    exec_time: str = None

    def __post_init__(self):
        type_checker(self)


@dataclass
class Order:
    id: str
    status: int
    title: str
    intro: str
    price: int
    owner_id: str
    start_time: str
    close_time: str
    exec_time: str
    connect_info: str

    def __post_init__(self):
        type_checker(self)


def type_checker(obj):
    for field in fields(obj):
        instance = getattr(obj, field.name)
        if instance is None:
            continue
        if type(getattr(obj, field.name)) != field.type:
            raise ValueError
