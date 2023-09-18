from app.database.util import create
from app.utils.time_util import get_current, date2str
from flask import request


def create_user():
    payload: dict = request.json
    create("account", payload)

    user_id = payload.get('id')
    current_time = date2str(get_current())
    item_ids = [
        "6fbd9679bd8b41239f584624af23e74b",
        "0b7e63b98e0143e980bd3c2c3e815f73",
        "820c69b5e95b40c5bf121a337a1f1cec",
        "e196fbb8fd934a9cbfd5d968c3dae18a",
        "4d5d21b000bf4a29bdb9c35c00d7da6d",
        "2acd5f723b4547818b70847c88357412"
    ]

    for item_id in item_ids:
        create("own_item", {
            "user_id":user_id,
            "item_id":item_id,
            "time": current_time
        })

    for item_id in item_ids[:3]:
        create("picked_item", {
            "user_id": user_id,
            "item_id": item_id,
        })


