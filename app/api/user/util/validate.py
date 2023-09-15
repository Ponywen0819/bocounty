from app.utils.respons_util import missing_required
from app.database.util import get
from .user import User
from .respons import conflict


def validate_create_payload_columns(values: dict):
    required_columns = _get_required_columns()
    for key in required_columns:
        value = values.get(key)
        if (value is None) and (type(value) != required_columns.get(key)):
            missing_required()

    validate_student_id(values.get("student_id"))
    validate_password(values.get("password"))


def validate_conflict(values: dict):
    users = get('account', {
        "student_id": values.get('student_id')
    })

    if len(users) != 0:
        conflict()


def validate_edit_payload(values: dict):
    pass


def validate_student_id(value):
    pass


def validate_name(value):
    pass


def validate_password(value):
    pass


def validate_bocoin(value):
    pass


def validate_intro(value):
    pass


def _get_required_columns() -> dict:
    user_columns: dict = User.__dict__["__annotations__"]
    return {
        "student_id": user_columns['student_id'],
        "password": user_columns["password"]
    }
