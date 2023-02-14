import json
import time
import hashlib
from datetime import datetime
from flask import Blueprint, jsonify, current_app, make_response, request
from modules.db_util import DatabaseUtils

auth = Blueprint('auth', __name__)


@auth.route('/test')
def test():

    return 'aaa'

@auth.route("/Register", methods=['POST'])
def register():
    """
    註冊使用者並且確認Email是否重複
        tags:
            - Login
        produces:
            - application/json
        parameters:
            - name: account_id
            - in: body
            - type: string
            - required: true
            - default: None
    """
    # connect database
    db = DatabaseUtils(ModuleFactory.AppConfig)
    
    # 取的是否辦過帳號了
    dbreturn = db.command_excute("""
        SELECT COUNT(*) 
        FROM account
        WHERE email = %(email)s 
    """, request.json)

    # success or fail return
    if len(dbreturn) != 0:
        return jsonify({
            'cause': 151
        })

    # 修感
    if len(request.json['password']) < 6:
        return jsonify({
            'cause': 152
        })
    require_field = ["id", "name", "email", "password"]
    for need in require_field:
        if need not in request.json.keys():
            return jsonify({"cause": 153})

    account_info = request.json
    # account_info['password'] = hashlib.sha256(current_app.config['crypto']
    #                                           .decrypt(request.json['password'])
    #                                           .encode("utf-8")).hexdigest()

    account_info['password'] = hashlib.sha256(
        ModuleFactory.Crypto.decrypt(request.json['password']).encode("utf-8")
    ).hexdigest()
    # 插入新的帳號
    db.command_excute("""
        INSERT INTO accounts (account_id, name, email, password) 
        VALUES (%(account_id)s, %(name)s, %(email)s, %(password)s)
    """, account_info)

    user_id = db.command_excute("""SELECT LAST_INSERT_ID() AS id;""", {})[0]['id']
    token = current_app.config['jwt'].generate_token({"user_id": user_id, "admin": 0})
    res = make_response(json.dumps({
        "cause": 0
    }))

    res.set_cookie("User_Token", token, expires=time.time() + 60 * 60)
    return res


@auth.route("Login", methods=['POST'])
def login():
    auth_info = request.json

    # auth_info['password'] = hashlib.sha256(current_app.config['crypto'].decrypt(request.json['password']).encode("utf-8")).hexdigest()

    auth_info['password'] = hashlib.sha256(
        ModuleFactory.Crypto.decrypt(request.json['password']).encode("utf-8")
    ).hexdigest()

    db = DatabaseUtils(ModuleFactory.AppConfig)
    # 確認有沒有此account
    dbreturn = db.command_excute("""
            SELECT 
                * 
            FROM 
                accounts 
            WHERE 
                email = %(account)s AND password = %(password)s
            """, auth_info)

    # 更新時間
    if len(dbreturn) == 1:
        db.command_excute("""
           UPDATE accounts
           SET last_login = %(date)s
           WHERE accounts.id = %(user_id)s
           """, {"user_id": dbreturn[0]['id'], "date": datetime.now().strftime("%Y/%m/%d %H:%M:%S")})
        token = current_app.config['jwt'].generate_token({"user_id": dbreturn[0]['id'], "admin": 0})
        res = make_response(json.dumps({
            "cause": 0
        }))

        res.set_cookie("User_Token", token, expires=time.time() + 60 * 60)
        return res
    elif len(dbreturn) > 1:
        return jsonify({"cause": 102})
    else:
        return jsonify({"cause": 101})


# @app.route("Logoff", methods=['POST'])
# def logoff():
#     if request.cookies.get('User_Token') is None: return "", 401
#     if not current_app.config['jwt'].check_token_valid(request.cookies.get('User_Token')):
#         return "", 401
#     user_info = current_app.config['jwt'].get_token_detail(request.cookies.get('User_Token'))
#     db = DatabaseUtils(ModuleFactory.AppConfig)
#     # 更新時間
#     if 'user_id' in user_info.keys():
#         db.command_excute("""
#             UPDATE accounts
#             SET last_login = %(date)s
#             WHERE accounts.id = %(user_id)s
#         """, {"user_id": user_info['user_id'], "date": datetime.now().strftime("%Y/%m/%d %H:%M:%S")})
#     res = make_response(json.dumps({
#         "cause": 0
#     }))
#     res.set_cookie("User_Token", "", expires=time.time() - 1)
#     return res
