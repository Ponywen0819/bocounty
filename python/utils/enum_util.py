from enum import Enum
from dataclasses import dataclass


@dataclass
class Code:
    http_code: int
    api_code: int


class APIStatusCode(Enum):
    NotLogin: Code = Code(http_code=401, api_code=200)
    NotGrant: Code = Code(http_code=401, api_code=201)
    Wrong_Format: Code = Code(http_code=400, api_code=202)
    RequireMissmatch: Code = Code(http_code=404, api_code=203)
    CoinNotEnough: Code = Code(http_code=200, api_code=204)


class OrderListCode(Enum):
    UsersOrder: int = 0
    InvolveInOrder: int = 1
    OpenOrder: int = 2
    AllOrder: int = 3
