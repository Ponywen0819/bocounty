from flask import current_app, request
from utils.jwt_util import JWTGenerator
from models import Account
from functools import wraps


def require_login(func):
    @wraps(func)
    def vertify(*args, **kwargs):
        jwt_gen: JWTGenerator = current_app.config['jwt_gen']
        token = request.cookies.get("User_Token")

        if token is None:
            print('token is None')
            return "", 301

        if not jwt_gen.check_token_valid(token):
            print('Token not valid')
            return "", 301

        token_info = jwt_gen.get_token_detail(token)

        user: Account = Account.query.filter(
            Account.id == token_info['user_id']
        ).first()

        if user is not None:
            return func(*args, **kwargs, user=user)
        else:
            return "", 301
    return vertify



