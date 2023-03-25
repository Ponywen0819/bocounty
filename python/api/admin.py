from flask import Blueprint, request, jsonify, current_app
import uuid
from sqlalchemy import func
from utils.auth_util import admin_required
from utils.respons_util import make_error_response
from utils.enum_util import APIStatusCode
from database import db
from models import Pool, Item, PoolItem
from utils.storage_util import StorgeCode, storage_photo, storage_delete


admin_api = Blueprint('admin_api', __name__)


@admin_api.route('/listPool', methods=['GET'])
@admin_required
def list_pool(*args, **kwargs):
    pools_and_counts = db.session.query(Pool.id, Pool.name, Pool.photo, func.count(Item.id)).\
        join(PoolItem, PoolItem.pool_id == Pool.id, isouter=True).\
        join(Item, Item.id == PoolItem.item_id, isouter=True).\
        group_by(Pool.id).all()
    pools_info = [
        dict(zip(['id', 'name', 'photo', 'num'], row))
        for row in pools_and_counts
    ]
    return jsonify({
        "status": 0,
        "pools": pools_info
    })


@admin_api.route('/createPool', methods=['POST'])
@admin_required
def create_pool(*args, **kwargs):
    req_json: dict = request.json

    new_pool_id = uuid.uuid4().hex
    new_pool_name = request.json['name']
    new_pool_photo_path = storage_photo(req_json['photo'], StorgeCode.POOL)

    if new_pool_photo_path is None:
        return make_error_response(APIStatusCode.Wrong_Format, reason='the format of photo data is not correct')

    new_pool = Pool(
        id=new_pool_id,
        name=new_pool_name,
        photo=new_pool_photo_path,
    )
    db.session.add(new_pool)
    db.session.commit()
    return jsonify({
        "status": 0,
        "pool_id": new_pool_id
    })


@admin_api.route('/deletePool', methods=['POST'])
@admin_required
def delete_pool(*args, **kwargs):
    pool: Pool = Pool.query.filter(
        Pool.id == request.json['id']
    ).first()

    if pool is None:
        return make_error_response(APIStatusCode.RequireMissmatch, reason="pool isn't exist")
    else:
        db.session.delete(pool)
        db.session.commit()
        return jsonify({
            "status": 0
        })


@admin_api.route('/modifyPoolItem', methods=['POST'])
@admin_required
def modify_pool_item(*args, **kwargs):
    pass


@admin_api.route('/listItem', methods=['GET'])
@admin_required
def list_item(*args, **kwargs):
    item_row = db.session.query(Item.id, Item.name, Item.photo, Item.type)
    item_list = [
        dict(zip(['id', 'name', 'photo', 'type'], row))
        for row in item_row
    ]
    return jsonify({
        "status": 0,
        "item_list": item_list
    })


@admin_api.route('/createItem', methods=['POST'])
@admin_required
def create_item(*args, **kwargs):
    req_json: dict = request.json

    new_item_id = uuid.uuid4().hex
    new_item_name = req_json['name']
    new_item_type = req_json['type']
    new_item_photo = storage_photo(req_json['photo'], StorgeCode.ITEM)

    new_item = Item(
        id=new_item_id,
        name=new_item_name,
        type=new_item_type,
        photo=new_item_photo
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({
        "status": 0,
        "pool_id": new_item_id
    })


@admin_api.route('/deleteItem', methods=['POST'])
@admin_required
def del_item(*args, **kwargs):
    item: Item = Item.query.filter(
        Pool.id == request.json['id']
    ).first()

    if item is None:
        return_code = 104
    else:
        db.session.delete(item)
        db.session.commit()
        return_code = 0
    return jsonify({
        "status": return_code
    })


@admin_api.route('/modifyItemInfo', methods=['POST'])
@admin_required
def modify_item_info(*args, **kwargs):
    req_json: dict = request.json
    item = Item.query.filter(
        Item.id == req_json['id']
    ).first()

    if item is None:
        return '', 406

    keys = req_json.keys()
    if 'name' in keys:
        item.name = req_json['name']
    if 'type' in keys:
        item.type = req_json['type']
    if 'photo' in keys:
        old_path = item.photo[5:]
        storage_delete(old_path, StorgeCode.ITEM)
        new_path = storage_photo(req_json['photo'], StorgeCode.ITEM)
        if new_path is None:
            return '', 406
        item.photo = new_path
    db.session.commit()
    return jsonify({
        'status': 0
    })
