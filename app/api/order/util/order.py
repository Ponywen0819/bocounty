from dataclasses import dataclass, fields


@dataclass
class CreatePayload:
    title: str
    intro: str
    price: int
    close_time: str
    exec_time: str = None

    def __post_init__(self):
        for field in fields(self):
            instance = getattr(self, field.name)
            if instance is None:
                continue
            if type(getattr(self, field.name)) != field.type:
                raise ValueError


@dataclass
class UpdatePayload:
    title: str
    intro: str
    close_time: str
    exec_time: str = None

    def __post_init__(self):
        for field in fields(self):
            instance = getattr(self, field.name)
            if instance is None:
                continue
            if type(getattr(self, field.name)) != field.type:
                raise ValueError


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

    def __post_init__(self):
        for field in fields(self):
            instance = getattr(self, field.name)
            if instance is None:
                continue
            if type(getattr(self, field.name)) != field.type:
                raise ValueError
