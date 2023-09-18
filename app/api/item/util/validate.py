from app.database.util import get
from app.utils.response import missing_required, wrong_format
from app.utils.response import not_found
from app.utils.auth.auth_util import get_login_user
from app.database.util import get
from flask import request

from .item import UpdateItem, Action
from .response import item_not_found


def validate_get_wear(student_id: str):
    _validate_user_exist(student_id)


def validate_update_wear():
    payload: dict = request.json

    try:
        UpdateItem(**payload)
    except TypeError:
        missing_required()
    except ValueError:
        wrong_format()


def _validate_user_exist(student_id: str):
    users = get('account', {
        "student_id": student_id
    })

    if len(users) != 1:
        not_found("user not found")


def validate_item_exist():
    payload: dict = request.json
    update_list: dict = payload.get('update_list')

    user = get_login_user()

    for update_action in update_list:
        action = Action(update_action.get('action'))
        if action == Action.EQUIP:
            items = get('own_item', {
                "user_id": user.get('id'),
                "item_id": update_action.get('item_id')
            })

            if len(items) != 1:
                item_not_found()
