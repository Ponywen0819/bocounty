from flask import Blueprint, current_app, request, jsonify
from models import Account, Item, OwnItem
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
            return '', 301
        else:
            return jsonify({
                'status': 0,
                'id': user.id,
                'name': user.name,
                'intro': user.intro
            })
    else:
        user: Account = kwargs["user"]
        return jsonify({
            'status': 0,
            'id': user.id,
            'name': user.name,
            'intro': user.intro
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
    pass


@account_api.route('/getUserCoin', methods=['GET'])
@require_login
def get_user_coin(*args, **kwargs):
    pass


@account_api.route('/changeUserInfo', method=['POST'])
@require_login
def change_user_info(*args, **kwargs):
    pass


@account_api.route('/changeUserOutlook', methods=['POST'])
@require_login
def change_user_outlook(*args, **kwargs):
    pass
