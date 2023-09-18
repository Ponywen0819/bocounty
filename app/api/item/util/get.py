from app.database.util import get
from .item import Item


def get_user_wearing(student_id: str):
    user = get('account', {
        "student_id": student_id
    })[0]

    user_wears = get('own_item', {
        "user_id": user.get('id')
    })

    res = []

    for user_wear in user_wears:
        item = get('item', {
            "id": user_wear.get('item_id')
        })[0]

        res.append(Item(item))

    return res
