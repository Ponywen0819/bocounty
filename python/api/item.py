from flask import current_app, Blueprint, request, jsonify
from utils.auth_util import login_required
from utils.respons_util import make_error_response
from utils.enum_util import APIStatusCode, DrawType
from utils.auth_util import get_user_by_token
from utils import get_now
from database import db
from models import Item, PoolItem, Pool, OwnItem, Account

import random

item_api = Blueprint("item_api", __name__)


@item_api.route('/getPoolItemList', methods=['POST'])
@login_required
def get_pool_item_list(*args, **kwargs):
    request_json: dict = request.json
    if 'id' not in request_json.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason='missing \'id\' argument!')

    pool_id = request_json['id']

    items = db.session.query(Item.id, Item.name, Item.photo). \
        join(PoolItem, PoolItem.item_id == Item.id). \
        join(Pool, Pool.id == PoolItem.pool_id). \
        filter(Pool.id == pool_id).all()

    item_info = [
        dict(zip(['id', 'name', 'photo'], [row.id, row.name, row.photo]))
        for row in items
    ]

    return jsonify({
        "status": 0,
        "items": item_info
    })


@item_api.route('/drawCards', methods=['POST'])
@login_required
def draw_cards(*args, **kwargs):
    request_json: dict = request.json

    user: Account = get_user_by_token()

    if 'pool' not in request_json.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason='missing \'pool\' argument!')

    if 'type' not in request_json.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason='missing \'type\' argument!')

    pool_id: int = request_json['pool']
    type: DrawType = DrawType(request_json['type'])

    items: list = db.session.query(Item.id, Item.name, Item.photo). \
        join(PoolItem, PoolItem.item_id == Item.id). \
        join(Pool, Pool.id == PoolItem.pool_id). \
        filter(Pool.id == pool_id)

    picked_items = []
    index_max = len(items) - 1
    times = 1 if type == DrawType.single else 10
    now_time = get_now()
    for i in range(times):
        picked_index = random.randint(0, index_max)
        picked_item: Item = items[picked_index]
        picked_items.append(picked_item)

        own_item_count = OwnItem.query.filter(
            OwnItem.user_id == user.id,
            OwnItem.item_id == picked_item.id
        ).count()
        if own_item_count == 0:
            db.session.add(OwnItem(
                user_id=user.id,
                item_id=picked_item.id,
                get_time=str(now_time)
            ))
    db.session.commit()

    picked_item_info = [
        dict(zip(['id', 'name', 'photo'], [row.id, row.name, row.photo]))
        for row in picked_items
    ]

    return jsonify({
        "status": 0,
        "list": picked_item_info
    })
