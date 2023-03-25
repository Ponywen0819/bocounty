from enum import Enum
from dataclasses import dataclass


@dataclass
class Code:
    http_code: int
    api_code: int


class APIStatusCode(Enum):
    NotLogin: Code = Code(http_code=401, api_code=200)
    NotGrant: Code = Code(http_code=401, api_code=200)
    Wrong_Format: Code = Code(http_code=400, api_code=201)
    RequireMissmatch: Code = Code(http_code=404, api_code=202)


