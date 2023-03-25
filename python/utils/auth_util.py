from flask import current_app, request, abort, jsonify
from utils.jwt_util import JWTGenerator
from utils.respons_util import make_error_response
from utils.enum_util import APIStatusCode
from models import Account
from functools import wraps


def verify_jwt(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if get_token_detail() is None:
            return 'require login', 401
        else:
            return func(*args, **kwargs)
    return wrap


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token_info = get_token_detail()
        if token_info is None:
            return make_error_response(APIStatusCode.NotLogin, reason='user has not token')

        user: Account = get_user_by_id(token_info['user_id'])
        if user is None:
            return make_error_response(APIStatusCode.NotLogin, reason='user not found')

        return func(*args, **kwargs)
    return wrapper


def get_user_by_id(user_id: str) -> Account:
    user: Account = Account.query.filter(
        Account.id == user_id
    ).first()

    return user


def get_token_detail():
    jwt_gen: JWTGenerator = current_app.config['jwt_gen']
    token = request.cookies.get("User_Token")

    if token is None:
        print('token is None')
        return None

    if not jwt_gen.check_token_valid(token):
        print('Token not valid')
        return None

    return jwt_gen.get_token_detail(token)

