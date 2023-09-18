from dataclasses import dataclass, fields
from enum import Enum, auto


class Action(Enum):
    REMOVE = auto()
    EQUIP = auto()

@dataclass
class Item:
    id: str
    name: str
    photo: str
    type: int


@dataclass
class UpdateItem:
    update_list: list

    def __post_init__(self):
        type_checker(self)

        for update_item in self.update_list:
            if type(update_item) != dict:
                raise ValueError
            UpdateAction(**update_item)


@dataclass
class UpdateAction:
    action: int
    item_id: str = None
    type: int = None

    def __post_init__(self):
        type_checker(self)

        action = Action(self.action)

        if (action == Action.EQUIP) and (self.item_id is None):
            raise TypeError

        if (action == Action.REMOVE) and (self.type is None):
            raise TypeError


def type_checker(obj):
    for field in fields(obj):
        instance = getattr(obj, field.name)
        if instance is None:
            continue
        if type(getattr(obj, field.name)) != field.type:
            raise ValueError
