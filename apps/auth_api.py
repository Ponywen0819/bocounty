import json
import time
import hashlib
from datetime import datetime
from flask import Blueprint, jsonify, current_app, make_response, request

from utils.db_util import DatabaseUtils
from utils.auth_util import *
from Enums.FlaskConfigEnum import FlaskConfigEnum as ConfigEnum
from modules import module_factory

auth = Blueprint('auth', __name__)


@auth.route("/Register", methods=['POST'])
def register():
    """
    註冊使用者並且確認Email是否重複
        tags:
            - Register
        produces:
            - application/json
        parameters:
            - name: str
            - email: str
            - password: str
    """
    # 初始化必要工具
    db = DatabaseUtils(current_app.config)
    factory: module_factory.ModuleFactory = current_app.config[ConfigEnum.Factory]

    # 確認帳號使否重複
    user_count = db.command_excute("""
        SELECT COUNT(*) 
        FROM account
        WHERE email = %(email)s 
    """, request.json)[0]['COUNT(*)']

    if user_count != 0:
        return jsonify({
            'cause': 101
        })

    # 確認註冊資料格式
    if len(request.json['password']) < 6:
        return jsonify({
            'cause': 102
        })
    require_field = ["name", "email", "password"]
    for need in require_field:
        if need not in request.json.keys():
            return jsonify({"cause": 102})

    account_info = request.json
    account_info['password'] = hashlib.sha256(
        factory.Crypto.decrypt(request.json['password']).encode("utf-8")
    ).hexdigest()

    print(account_info)

    # 插入新的帳號
    db.command_excute("""
        INSERT INTO account (name, email, password)
        VALUES (%(name)s, %(email)s, %(password)s)
    """, account_info)

    user_id = db.command_excute("""SELECT LAST_INSERT_ID() AS id;""", {})[0]['id']
    token = factory.JWTGenerator.generate_token({"user_id": user_id, "admin": 0})
    res = make_response(json.dumps({
        "cause": 0
    }))

    res.set_cookie("User_Token", token, expires=time.time() + 60 * 60)
    return res


@auth.route("Login", methods=['POST'])
def login():
    """
        用於驗證使用者登入資訊，並發放token

        :parameter:
            - name: str
            - email: str
            - password: str
        :return:
            - application/json
    """
    factory = current_app.config[ConfigEnum.Factory]
    db = DatabaseUtils(current_app.config)

    auth_info = request.json
    auth_info['password'] = hashlib.sha256(
        factory.Crypto.decrypt(request.json['password']).encode("utf-8")
    ).hexdigest()

    # 確認有沒有此account
    user_info = db.command_excute("""
        SELECT id 
        FROM account 
        WHERE email = %(email)s AND password = %(password)s
    """, auth_info)

    if len(user_info) == 1:
        token = factory.JWTGenerator.generate_token({"user_id": user_info[0]['id'], "admin": 0})
        res = make_response(json.dumps({
            "cause": 0
        }))
        res.set_cookie("User_Token", token, expires=time.time() + 60 * 60)
        return res
    else:
        return jsonify({"cause": 102})


@auth.route("Logoff", methods=['POST'])
def logoff():
    factory = current_app.config[ConfigEnum.Factory]

    if request.cookies.get('User_Token') is None:
        return "", 401
    if not factory.JWTGenerator.check_token_valid(request.cookies.get('User_Token')):
        return "", 401

    res = make_response(json.dumps({
        "cause": 0
    }))
    res.set_cookie("User_Token", "", expires=time.time() - 1)
    return res
