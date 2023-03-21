import json
import time
from datetime import datetime, timedelta
import hashlib
import uuid
from utils.jwt_util import JWTGenerator
from utils.auth_util import require_login

from flask import Blueprint, jsonify, make_response, Response, request, current_app

from database import db
from models import Account, PickedItem


auth_api = Blueprint('auth_api', __name__)


@auth_api.route("/Register", methods=['POST'])
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
    require_field = ["student_id", "name", "password"]
    for need in require_field:
        if need not in request.json.keys():
            return jsonify({"cause": 102})

    # 確認帳號使否重複
    user_count = Account.query.filter(
        Account.student_id == request.json["student_id"]
    ).count()

    if user_count != 0:
        return jsonify({
            'cause': 101
        })

    account_info = request.json
    account_info['password'] = hashlib.sha256(request.json['password'].encode("utf-8")).hexdigest()

    # 插入新的帳號
    new_id = uuid.uuid4().hex

    new_account = Account(
        id=new_id,
        student_id=account_info['student_id'],
        name=account_info['name'],
        password=account_info['password']
    )
    db.session.add(new_account)
    db.session.commit()

    # token = factory.JWTGenerator.generate_token({"user_id": new_id})
    res = make_response(json.dumps({"cause": 0}))

    token_setter(name="User_Token", respond=res,
                 payload={"user_id": new_id})
    # res.set_cookie("User_Token", token, expires=time.time() + 60 * 60)
    return res


@auth_api.route("/Login", methods=['POST'])
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
    auth_info = request.json
    auth_info['password'] = hashlib.sha256(request.json['password'].encode("utf-8")).hexdigest()
    # 確認有沒有此account
    user: Account = Account.query.filter(
        Account.student_id == auth_info['student_id'],
        Account.password == auth_info['password']
    ).first()

    if user is not None:
        res = make_response(json.dumps({"cause": 0}))
        token_setter(name="User_Token", respond=res,
                     payload={"user_id": user.id})
        return res
    else:
        return jsonify({"cause": 102})


@auth_api.route("/Logoff", methods=['POST'])
def logoff():
    jwt_gen: JWTGenerator = current_app.config['jwt_gen']

    if request.cookies.get('User_Token') is None:
        return "", 401
    if not jwt_gen.check_token_valid(request.cookies.get('User_Token')):
        return "", 401

    res = make_response(json.dumps({
        "cause": 0
    }))
    res.set_cookie("User_Token", "", expires=time.time() - 1)
    return res


def token_setter(
        name: str,
        respond: Response,
        payload: dict,
        time: timedelta = timedelta(days=1)) -> None:
    jwt_gen: JWTGenerator = current_app.config['jwt_gen']
    jwt = jwt_gen.generate_token(payload)
    respond.set_cookie(name, value=jwt, expires=datetime.now() + time)
