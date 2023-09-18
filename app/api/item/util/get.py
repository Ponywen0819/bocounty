from app.database.util import get
from app.utils.auth.auth_util import get_login_user

from .item import Item


def get_user_wearing(student_id: str):
    user = get('account', {
        "student_id": student_id
    })[0]

    user_wears = get('picked_item', {
        "user_id": user.get('id')
    })

    return convert_id2dict(user_wears)

def get_user_own():
    user = get_login_user()

    item_list = get('own_item',{
        "user_id": user.get('id')
    })

    return convert_id2dict(item_list)

def convert_id2dict(item_list: list):
    res = []

    for item_data in item_list:
        item = get('item', {
            "id": item_data.get('item_id')
        })[0]

        res.append(Item(**item))

    return res