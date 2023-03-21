from flask import current_app, request
from utils.jwt_util import JWTGenerator
from models import Account
from functools import wraps


def require_login(func):
    @wraps(func)
    def verify(*args, **kwargs):
        token_info = _get_token_detail()
        if token_info is None:
            return '操', 401
        user: Account = Account.query.filter(
            Account.id == token_info['user_id']
        ).first()

        if user is not None:
            return func(*args, **kwargs, user=user)
        else:
            return "", 401
    return verify


def require_admin(func):
    @wraps(func)
    def verify(*args, **kwargs):
        token_info = _get_token_detail()
        if token_info is None:
            return '', 401
        user: Account = Account.query.filter(
            Account.id == token_info['user_id']
        ).first()

        if user is None:
            return "", 401
        elif user.permission != 1:
            return "", 401
        else:
            return func(*args, **kwargs, user=user)
    return verify


def require_vertify(func):
    @wraps(func)
    def vertify(*args, **kwargs):
        token_info = _get_token_detail()
        user: Account = Account.query.filter(
            Account.id == token_info['user_id']
        ).first()

        if user.mail_verify == 1:
            return func(*args, **kwargs, user=user)
        else:
            return "", 401
    return vertify


def _get_token_detail():
    jwt_gen: JWTGenerator = current_app.config['jwt_gen']
    token = request.cookies.get("User_Token")

    if token is None:
        print('token is None')
        return None

    if not jwt_gen.check_token_valid(token):
        print('Token not valid')
        return None

    return jwt_gen.get_token_detail(token)
