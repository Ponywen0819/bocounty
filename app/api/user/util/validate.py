from flask import request
from app.utils.response import wrong_format, missing_required, not_found
from app.utils.auth.auth_util import get_login_user
from app.database.util import get
from .user import CreateUser, EditUser
from .respons import conflict, no_permission


def validate_get(student_id: str):
    _validate_user_exist(student_id)


def validate_create_payload():
    payload: dict = request.json
    try:
        CreateUser(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()

    _validate_conflict()


def validate_edit_payload(student_id: str):
    payload: dict = request.json
    try:
        EditUser(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()

    _validate_name_not_null()
    _validate_permission(student_id)


def _validate_conflict():
    payload: dict = request.json
    users = get('account', {
        "student_id": payload.get('student_id')
    })

    if len(users) != 0:
        conflict()


def _validate_name_not_null():
    payload: dict = request.json
    name = payload.get('name')
    if name is None:
        return

    while len(name) > 0:
        if name[0] == " ":
            name = name[1:]
        else:
            break

    if name == "":
        wrong_format()


def _validate_permission(student_id: str):
    user = get_login_user()
    if user.get("student_id") != student_id:
        no_permission()


def _validate_user_exist(student_id: str):
    users = get('account', {
        "student_id": student_id
    })

    if len(users) != 1:
        not_found("user not found")
