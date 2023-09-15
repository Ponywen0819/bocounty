from app.utils.respons_util import wrong_format, missing_required, not_verified
from app.database.util import get


def validate_login_payload(payload: dict):
    required_column = ["student_id", "password"]
    for column in required_column:
        value = payload.get(column)
        if value is None:
            missing_required()

        if type(value) != str:
            wrong_format()

def validate_registe_payload(payload: dict):
    required_col


def validate_conflict(payload):
    users = get('account', payload)
    if len(users) != 0:
        raise


def validate_verify_status(user: dict):
    if user.get("verify") == 0:
        not_verified()
