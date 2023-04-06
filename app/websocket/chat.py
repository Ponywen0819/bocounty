from .. import socket
from flask_socketio import emit, send, ConnectionRefusedError
from flask import session, request
from app.utils.auth_util import check_login, get_user_by_token, login_required
from app.models import Account


@socket.on('connect')
def test_connect(auth):
    print(auth)
    login_state = check_login()
    if login_state != 0:
        return False
    user: Account = get_user_by_token()
    session[user.id]: str = request.sid
    emit('join', {'data': 42})


@socket.on('send')
def sendd_msg(data):
    print()
    emit('join', {'data': 42})
