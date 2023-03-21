import uuid
from sqlalchemy import func
from flask import Blueprint, request, jsonify
from utils.auth_util import require_admin
from database import db
from models import Pool, Item, PoolItem
from utils.storage_util import StorgeCode, storage_photo


admin_api = Blueprint('admin_api', __name__)


@admin_api.route('/listPool', methods=['GET'])
@require_admin
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
@require_admin
def create_pool(*args, **kwargs):
    req_json: dict = request.json

    new_pool_id = uuid.uuid4().hex
    new_pool_name = request.json['name']
    new_pool_photo_path = storage_photo(req_json['photo'], StorgeCode.POOL)

    if new_pool_photo_path is None:
        return '', 406

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
@require_admin
def delete_pool(*args, **kwargs):
    pool: Pool = Pool.query.filter(
        Pool.id == request.json['id']
    ).first()

    if pool is None:
        return_code = 104
    else:
        db.session.delete(pool)
        db.session.commit()
        return_code = 0
    return jsonify({
        "status": return_code
    })


@admin_api.route('/modifyPoolItem', methods=['POST'])
@require_admin
def modify_pool_item(*args, **kwargs):
    pass


@admin_api.route('/listItem', methods=['GET'])
@require_admin
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
@require_admin
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
@require_admin
def del_item(*args, **kwargs):
    pass
