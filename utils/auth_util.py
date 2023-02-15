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
            return "", 301
        if factory.JWTGenerator.check_token_valid(token):
            return "", 301
        user_info = factory.JWTGenerator.get_token_detail(token)

        user_count = db.command_excute('''
            SELECT COUNT(*)
            FROM account
            WHERE account.id = %(user_id)s
        ''', user_info)[0]['COUNT(*)']

        if user_count != 0:
            return "", 301
        return func(*args, **kwargs)
    return vertify
