from flask import current_app, request
from Enums.FlaskConfigEnum import FlaskConfigEnum as ConfigEnum
from modules.module_factory import ModuleFactory
from utils.db_util import DatabaseUtils
from functools import wraps


def require_login(func):
    @wraps(func)
    def vertify(*args, **kwargs):
        # initial
        factory: ModuleFactory = current_app.config[ConfigEnum.Factory]
        db = DatabaseUtils(current_app.config)
        token = request.cookies.get("User_Token")

        if token is None:
            print("Token nor excite")
            return "", 301

        if not factory.JWTGenerator.check_token_valid(token):
            print("Token not valid")
            return "", 301

        token_info = factory.JWTGenerator.get_token_detail(token)

        user_info = db.command_excute('''
            SELECT *
            FROM account
            WHERE account.id = %(user_id)s
        ''', token_info)

        if len(user_info) != 1:
            return "", 301
        return func(*args, **kwargs, user_info=user_info[0], db=db)
    return vertify



