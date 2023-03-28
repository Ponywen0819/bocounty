import os
import secrets
import uuid
from utils.jwt_util import JWTGenerator
from flask import Flask, render_template, redirect
from api.auth import auth_api
from api.account import account_api
from api.admin import admin_api
from api.order import order_api
from api.item import item_api
from api.message import message_api

from models import Account, PickedItem, Item


def create_app(config_filename=None):
    app = Flask(__name__, template_folder='../template', static_folder='../src')
    if config_filename is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_pyfile(config_filename)
    app.config['jwt_gen']: JWTGenerator = JWTGenerator()

    from database import db, create_db
    db.init_app(app)

    with app.app_context():
        create_db(flush=False)

    app.register_blueprint(auth_api)
    app.register_blueprint(account_api)
    app.register_blueprint(admin_api)
    app.register_blueprint(order_api)
    app.register_blueprint(item_api)
    # app.register_blueprint(message_api)

    from models import Order, Involve
    from sqlalchemy import func
    from utils.enum_util import OrderListCode

    @app.route('/')
    def to_admin_page():
        return redirect('/test')

    @app.route('/test/<path>')
    @app.route('/test')
    def admin_page(path=None):
        setting = {
            "title": '管業員頁面',
        }
        return render_template('main.html', setting=setting)

    return app
