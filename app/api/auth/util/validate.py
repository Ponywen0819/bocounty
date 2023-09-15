from .response import missing_required, wrong_format, not_verified
from app.database.util import get


def validate_login_payload(payload: dict):
    required_column = ["student_id", "password"]
    for column in required_column:
        value = payload.get(column)
        if value is None:
            missing_required()

        if type(value) != str:
            wrong_format()


def validate_verify_status(user: dict):
    if user.get("verify") == 0:
        not_verified()
