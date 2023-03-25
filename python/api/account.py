from flask import Blueprint, current_app, request, jsonify
from models import Account, Item, OwnItem, PickedItem
from database import db
from utils.auth_util import login_required, get_token_detail, get_user_by_id
from utils.enum_util import APIStatusCode
from utils.respons_util import make_error_response

account_api = Blueprint("acc_api", __name__)


# @account_api.route('/getUserInfo/<id>', methods=['GET'])
@account_api.route('/getUserInfo', methods=['GET'])
@login_required
def get_user_info(*args, **kwargs):
    if 'id' in request.json.keys():
        require_id = request.json['id']
    else:
        token_info = get_token_detail()
        require_id = token_info['user_id']

    user: Account = get_user_by_id(require_id)
    if user is None:
        return make_error_response(APIStatusCode.RequireMissmatch, reason="user isn't exist")
    return jsonify({
        'status': 0,
        'id': user.id,
        'name': user.name,
        'intro': user.intro,
        'bocoin': user.bocoin
    })


@account_api.route('/checkUserVerify', methods=['GET'])
@login_required
def check_user_verify(*args, **kwargs):
    token_info = get_token_detail()
    user: Account = get_user_by_id(token_info['user_id'])
    if user is None:
        return make_error_response(APIStatusCode.NotLogin, reason='require login')

    verify_state = 1 if user.mail_verify == 1 else 0

    return jsonify({
        "status": 0,
        "verify": verify_state
    })


@account_api.route('/getUserItem', methods=['GET'])
@login_required
def get_user_item(*args, **kwargs):
    token_info = get_token_detail()
    user: Account = get_user_by_id(token_info['user_id'])

    item_list = Item.query.\
        join(OwnItem, OwnItem.item_id == Item.id).\
        join(Account, Account.id == OwnItem.user_id).\
        filter(Account.id == user.id).all()

    return jsonify({
        'status': 0,
        "list": item_list
    })


@account_api.route('/getUserOutlook', methods=['GET'])
@login_required
def get_user_outlook(*args, **kwargs):
    token_info = get_token_detail()
    user: Account = get_user_by_id(token_info['user_id'])

    item_list, equ_types = db.session.query(Item, PickedItem.type).\
        join(PickedItem, Item.id == PickedItem.item_id).\
        join(Account, Account.id == PickedItem.user_id).\
        fliter(PickedItem.user_id == user.id).\
        all()

    for item, equ_type in zip(item_list, equ_types):
        print(item.type, equ_type)

    return '', 200


@account_api.route('/getUserCoin', methods=['GET'])
@login_required
def get_user_coin(*args, **kwargs):
    token_info = get_token_detail()
    user: Account = get_user_by_id(token_info['user_id'])

    return jsonify({
        'status': 0,
        'num': user.bocoin
    })


@account_api.route('/changeUserInfo', methods=['POST'])
@login_required
def change_user_info(*args, **kwargs):
    token_info = get_token_detail()
    user: Account = get_user_by_id(token_info['user_id'])

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
@login_required
def change_user_outlook(*args, **kwargs):
    pass

