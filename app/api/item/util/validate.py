from app.database.util import get
from app.utils.response import not_found


def validate_get_wear(student_id: str):
    _validate_user_exist(student_id)


def validate_update_wear(student_id: str):
    _validate_user_exist(student_id)


def _validate_user_exist(student_id: str):
    users = get('account', {
        "student_id": student_id
    })

    if len(users) != 1:
        not_found("user not found")
