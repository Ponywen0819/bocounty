from .validate import validate_create_payload_columns, validate_conflict
from app.database.util import create
from hashlib import sha256
from uuid import uuid4


def create_user(values: dict) -> str:
    new_id: str = uuid4().hex
    values['id'] = new_id
    validate_create_payload_columns(values)
    validate_conflict(values)
    create("account", {
        "id": new_id,
        "student_id": values["student_id"],
        "name": "新進冒險者",
        "password": sha256(values["password"].encode("utf-8")).hexdigest(),
        "bocoin": 0,
        "intro": "留下你的自我介紹吧!",
        "verify": 0,
        "role": 0
    })

    return new_id
