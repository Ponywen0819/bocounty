from flask import Blueprint, current_app, request, jsonify
from models import Account, Item, OwnItem, PickedItem
from database import db
from utils.auth_util import require_login

account_api = Blueprint("acc_api", __name__)


# @account_api.route('/getUserInfo/<id>', methods=['GET'])
@account_api.route('/getUserInfo', methods=['GET'])
@require_login
def get_user_info(*args, **kwargs):
    if 'id' in request.json.keys():
        user: Account = Account.query.filter(
            Account.id == request.json['id']
        ).first()

        if user is None:
            return '', 401
    else:
        user: Account = kwargs["user"]
    return jsonify({
        'status': 0,
        'id': user.id,
        'name': user.name,
        'intro': user.intro,
        'bocoin': user.bocoin
    })


@account_api.route('/checkUserVerify', methods=['GET'])
@require_login
def check_user_verify(*args, **kwargs):
    user: Account = kwargs['user']
    if user.mail_verify == 1:
        verify_state = 1
    else:
        verify_state = 0
    return jsonify({
        "status": 0,
        "verify": verify_state
    })


@account_api.route('/getUserItem', methods=['GET'])
@require_login
def get_user_item(*args, **kwargs):
    user: Account = kwargs['user']
    item_list = Item.query.\
        join(OwnItem, OwnItem.item_id == Item.id).\
        join(Account, Account.id == OwnItem.user_id).\
        filter(Account.id == user.id).all()

    return jsonify({
        'status': 0,
        "list": item_list
    })


@account_api.route('/getUserOutlook', methods=['GET'])
@require_login
def get_user_outlook(*args, **kwargs):
    user: Account = kwargs['user']
    item_list, equ_types = db.session.query(Item, PickedItem.type).\
        join(PickedItem, Item.id == PickedItem.item_id).\
        join(Account, Account.id == PickedItem.user_id).\
        all()
    for item, equ_type in zip(item_list,equ_types):
        print(item.type, equ_type)

    return '', 200


@account_api.route('/getUserCoin', methods=['GET'])
@require_login
def get_user_coin(*args, **kwargs):
    user: Account = kwargs['user']
    return jsonify({
        'status': 0,
        'num': user.bocoin
    })


@account_api.route('/changeUserInfo', methods=['POST'])
@require_login
def change_user_info(*args, **kwargs):
    user: Account = kwargs['user']
    req_json: dict = request.json
    if 'name' in req_json.keys():
        user.name = req_json['name']
    if 'intro' in req_json.keys():
        user.intro = req_json['intro']
    db.session.commit()

    return jsonify({
        'status': 0
    })


@account_api.route('/changeUserOutlook', methods=['POST'])
@require_login
def change_user_outlook(*args, **kwargs):
    pass
