from random import randint
from app.database.util import update, get, create
from app.utils.auth.auth_util import get_login_user
from app.utils.time_util import get_current, date2str

from .pool import PoolItem

from flask import request

from .pool import DrawType
from .get import get_pool_item


def draw_card():
    payload: dict = request.json

    type = DrawType(payload["type"])

    item_list = get_pool_item("pool_id")

    num = 0
    if type == DrawType.single:
        num = 1
    elif type == DrawType.multi:
        num = 10

    res = []
    for i in range(num):
        picked = randint(0, len(item_list))
        res.append(item_list[picked])

    update_item(res)

    return res


def update_item(item_list: list[PoolItem]):
    user = get_login_user()
    current = date2str(get_current())

    for item in item_list:
        items = get('own_pool', {
            "user_id": user.get('id'),
            "item_id": item.item_id
        })

        if len(items) != 0:
            continue

        create('own_pool', {
            "user_id": user.get('id'),
            "item_id": item.item_id,
            "time": current
        })
