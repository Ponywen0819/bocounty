from __future__ import annotations

from app.database.util import get
from .respons import not_found
from .user import User


def get_user_list() -> list:
    datas = get("account")

    return [User(**data) for data in datas]


def get_user(student_id: str) -> User | None:
    data = get("account", {
        "student_id": student_id
    })

    return User(**data[0])
