from flask import request
from app.database.util import update
from app.utils.auth.auth_util import get_login_user


def edit_user():
    payload: dict = request.json
    user = get_login_user()
    update('account', {
        "id": user.get('id')
    }, payload)
