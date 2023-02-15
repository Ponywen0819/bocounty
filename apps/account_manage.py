import json
import time
import hashlib
from datetime import datetime
from flask import Blueprint, jsonify, current_app, make_response, request

from utils.db_util import DatabaseUtils
from utils.auth_util import *
from Enums.FlaskConfigEnum import FlaskConfigEnum as ConfigEnum
from modules import module_factory

account = Blueprint('account', __name__)


@account.route('/getUserInfo/<id>', methods=['GET'])
@account.route('/getUserInfo', methods=['GET'])
@require_login
def get_user_info(*args, **kwargs):
    user_info = kwargs["user_info"]
    if ('id' in kwargs.keys()) and (kwargs['id'] != user_info['id']):
        db = kwargs['db']
        others_info = db.command_excute('''
            SELECT email, intro, name
            FROM account
            WHERE id = %(id)s
        ''', kwargs)

        if len(others_info) >= 1:
            return jsonify({
                "status": 101
            })
        elif len(others_info) == 0:
            return jsonify({
                "status": 102
            })
        else:
            others_info = others_info[0]
            return jsonify({
                "status": 0,
                "email": others_info['email'],
                "intro": others_info["intro"],
                "name": others_info["name"]
            })
    else:
        return jsonify({
            "status": 0,
            "email": user_info['email'],
            "intro": user_info["intro"],
            "name": user_info["name"]
        })


@account.route('/getUserItem', methods=['GET'])
@require_login
def get_user_login(*args, **kwargs):
    user_info = kwargs["user_info"]
    db: DatabaseUtils = kwargs["db"]

    clothe_list = db.command_excute('''
        SELECT
	        own_clothe.owner_id as owner_id, 
	        clothe.id as clothe_id, 
	        clothe.type as type, 
	        clothe.photo as photo
        FROM
	        own_clothe INNER JOIN clothe ON own_clothe.clothe_id = clothe.id
	    WHERE
	        own_clothe.owner_id = %(id)s
    ''',user_info)

    return jsonify({
        'status': 0,
        "list": clothe_list
    })

# @account.route('/get')