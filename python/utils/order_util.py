from dataclasses import dataclass
from flask import request
from functools import wraps
from datetime import datetime
import re


@dataclass
class CreateOrderPayload:
    title: str
    close_time: str
    exec_time: str
    price: int
    intro: str

    def __post_init__(self):
        self.close_time = str(datetime.fromisoformat(self.close_time))
        if self.exec_time != 'None':
            self.exec_time = str(datetime.fromisoformat(self.exec_time))


@dataclass
class SpecifyOrderPayload:
    id: str


@dataclass
class GetOrderPayload:
    type: int


def verify_create_form(func):
    @wraps
    def wrap(*args, **kwargs):
        request_json: dict = request.json

        if request_json is None:
            return '', 406
        try:
            payload = CreateOrderPayload(**request_json)
        except TypeError:
            return '', 406

        return func(*args, **kwargs)
    return wrap
