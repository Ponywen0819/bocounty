from app.utils.jwt_util import JWTGenerator
from app.utils.respons_util import make_error_response
from app.utils.enum_util import APIStatusCode, LoginState
from app.utils.email_util import send_verify_email
from app.models import Account
from app.database import db
from flask import current_app, request, abort, jsonify, Flask
from functools import wraps
import threading
from uuid import uuid4


def register(student_id: str, name: str, password: str) -> Account:
    user_count = Account.query.filter(
        Account.student_id == student_id
    ).count()
    if user_count != 0:
        return None

    # 插入新的帳號
    new_id = uuid4().hex

    new_user = Account(
        id=new_id,
        student_id=student_id,
        name=name,
        password=password
    )
    db.session.add(new_user)
    db.session.commit()

    setting: dict = current_app.config["setting"]
    if setting["mail"]["enable"]:
        thread = FlaskThread(
            target=send_verify_email, args=[new_user.student_id, new_user.name])
        thread.start()

    return new_user


def verify_jwt(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if _get_token_detail() is None:
            return 'require login', 401
        else:
            return func(*args, **kwargs)

    return wrap


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        login_state = check_login()

        if login_state == LoginState.TokenMiss:
            return make_error_response(APIStatusCode.NotLogin, reason='user has not token')
        if login_state == LoginState.UserNotFound:
            return make_error_response(APIStatusCode.NotLogin, reason='user not found')
        if login_state == LoginState.NotVerify:
            return make_error_response(APIStatusCode.NotLogin, reason='user not verified')

        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        login_state = check_login(admin=True)

        if login_state == LoginState.TokenMiss:
            return make_error_response(APIStatusCode.NotLogin, reason='user has not token')
        if login_state == LoginState.UserNotFound:
            return make_error_response(APIStatusCode.NotLogin, reason='user not found')
        if login_state == LoginState.NotVerify:
            return make_error_response(APIStatusCode.NotLogin, reason='user not verified')
        if login_state != LoginState.AdminSucess:
            return make_error_response(APIStatusCode.NotGrant, reason='user has no permission')

        return func(*args, **kwargs)

    return wrapper


def get_user_by_token():
    token_info = _get_token_detail()
    user: Account = Account.query.filter(
        Account.id == token_info['user_id']
    ).first()

    return user


def check_login() -> LoginState:
    token_info = _get_token_detail()
    if token_info is None:
        return LoginState.TokenMiss

    user: Account = Account.query.filter(
        Account.id == token_info['user_id']
    ).first()
    if user is None:
        return LoginState.UserNotFound
    if user.permission == 1:
        return LoginState.AdminSucess
    setting: dict = current_app.config["setting"]
    if setting["mail"]["enable"]:
        if user.mail_verify == 0:
            return LoginState.NotVerify
    return LoginState.UserSuccess


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


class FlaskThread(threading.Thread):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # type: ignore[attr-defined]
        self.app: Flask = current_app._get_current_object()

    def run(self) -> None:
        with self.app.app_context():
            super().run()
