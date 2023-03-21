from dataclasses import dataclass
from flask import request
from functools import wraps
import re


@dataclass
class CreateOrderPayload:
    title: str
    close_time: str
    exec_time: str
    price: int
    intro: str
    def __post_init__(self):

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
