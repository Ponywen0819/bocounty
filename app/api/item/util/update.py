from app.database.util import delete, get, create, update
from app.utils.auth.auth_util import get_login_user
from flask import request

from .item import Action


def update_wear():
    payload: dict = request.json
    update_list: list[dict] = payload.get('update_list')

    for update_item in update_list:
        action = Action(update_item.get('action'))
        item_id = update_item.get('item_id')
        item_type = update_item.get('type')

        if action == Action.REMOVE:
            remove_item(item_type)

        elif action == Action.EQUIP:
            equip_item(item_id)


def remove_item(item_type: int):
    user = get_login_user()

    old_item_list = get('picked_item', {
        "user_id": user.get("id")
    })

    for old_item_data in old_item_list:
        old_item = get('item', {
            "id": old_item_data.get('item_id')
        })[0]

        if old_item.get('type') == item_type:
            delete('picked_item', {
                "user_id": user.get("id"),
                "item_id": old_item.get('id')
            })


def equip_item(item_id: str):
    user = get_login_user()
    item = get('item', {
        "id": item_id
    })[0]

    old_item_list = get('picked_item', {
        "user_id": user.get("id")
    })

    conflict_item = None

    for old_item_data in old_item_list:
        old_item = get('item', {
            "id": old_item_data.get('item_id')
        })[0]

        if old_item.get('type') == item.get('type'):
            conflict_item = old_item
            break

    if conflict_item is None:
        create('picked_item', {
            "user_id": user.get("id"),
            "item_id": item_id
        })
    else:
        update('picked_item', {
            "item_id": conflict_item.get('id'),
            "user_id": user.get("id")
        }, {"item_id": item_id})
