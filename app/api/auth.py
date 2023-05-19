import json
import time
from datetime import datetime, timedelta
import hashlib
import uuid
from app.utils.jwt_util import JWTGenerator
from app.utils.respons_util import make_error_response
from app.utils.enum_util import APIStatusCode
from app.utils.auth_util import register

from flask import Blueprint, jsonify, make_response, Response, request, current_app

from app.database import db
from app.models import Account, PickedItem

auth_api = Blueprint('auth_api', __name__)


@auth_api.route("/Register", methods=['POST'])
def register_route():
    request_json: dict = request.json
    if "student_id" not in request_json.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason="missing 'student_id' argument!")
    student_id = request_json["student_id"]

    if "name" not in request_json.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason="missing 'name' argument!")
    user_name = request_json["name"]

    if "password" not in request_json.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason="missing 'password' argument!")
    user_passwd = request_json["password"]

    user_passwd = hashlib.sha256(user_passwd.encode("utf-8")).hexdigest()

    user: Account = register(student_id, user_name, user_passwd)

    if user == None:
        return make_error_response(APIStatusCode.Wrong_Format, reason="Account is already exsit!")

    res = make_response(json.dumps({"cause": 0}))
    token_setter(name="User_Token", respond=res,
                 payload={"user_id": user.id})
    return res


@auth_api.route("/Login", methods=['POST'])
def login():
    auth_info: dict = request.json
    if "student_id" not in auth_info.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason="missing 'student_id' argument!")
    if "password" not in auth_info.keys():
        return make_error_response(APIStatusCode.Wrong_Format, reason="missing 'password' argument!")

    auth_info['password'] = hashlib.sha256(
        request.json['password'].encode("utf-8")).hexdigest()
    # 確認有沒有此account
    user: Account = Account.query.filter(
        Account.student_id == auth_info['student_id'],
        Account.password == auth_info['password']
    ).first()

    if user is not None:
        res = make_response(json.dumps({"status": 0}))
        token_setter(name="User_Token", respond=res,
                     payload={"user_id": user.id})
        return res
    else:
        return make_error_response(APIStatusCode.WrongLoginInfo, reason='wrong password or id!')


@auth_api.route("/Loginadmin", methods=['POST'])
def loginadmin():
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
    auth_info['password'] = hashlib.sha256(
        request.json['password'].encode("utf-8")).hexdigest()
    # 確認有沒有此account
    user: Account = Account.query.filter(
        Account.student_id == auth_info['student_id'],
        Account.password == auth_info['password'],
        Account.permission == 1
    ).first()

    if user is not None:
        res = make_response(json.dumps({"status": 0}))
        token_setter(name="User_Token", respond=res,
                     payload={"user_id": user.id})
        return res
    else:
        return make_error_response(APIStatusCode.WrongLoginInfo, reason='wrong password or id!')


@auth_api.route("/Logoff", methods=['POST'])
def logoff():
    jwt_gen: JWTGenerator = current_app.config['jwt_gen']

    if request.cookies.get('User_Token') is None:
        return "", 401
    if not jwt_gen.check_token_valid(request.cookies.get('User_Token')):
        return "", 401

    res = make_response(json.dumps({
        "status": 0
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
