from flask import Flask, render_template, redirect
from flask_socketio import SocketIO

socket = SocketIO()


def create_app(config_filename=None):
    app = Flask(__name__, template_folder='../template', static_folder='../src')
    if config_filename is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_pyfile(config_filename)

    from app.utils.jwt_util import JWTGenerator
    # from .utils.jwt_util import JWTGenerator
    app.config['jwt_gen']: JWTGenerator = JWTGenerator()
    # app.debug = True

    from app.database import db, create_db
    db.init_app(app)

    with app.app_context():
        create_db(flush=False)

    from app.api.auth import auth_api
    from app.api.account import account_api
    from app.api.admin import admin_api
    from app.api.order import order_api
    from app.api.item import item_api
    from app.api.message import message_api

    app.register_blueprint(auth_api)
    app.register_blueprint(account_api)
    app.register_blueprint(admin_api)
    app.register_blueprint(order_api)
    app.register_blueprint(item_api)
    app.register_blueprint(message_api)

    socket.init_app(app)
    return app
