import os
import secrets
import uuid
from utils.jwt_util import JWTGenerator
from flask import Flask
from api.auth import auth_api
from api.account import account_api
from api.item import item_api
from api.admin import admin_api
from api.message import message_api
from api.order import order_api

from models import Account, PickedItem, Item


def create_app(config_filename=None):
    app = Flask(__name__)
    if config_filename is None:
        app.config.from_pyfile('config.py')
    else:
        app.config.from_pyfile(config_filename)
    app.config['jwt_gen']: JWTGenerator = JWTGenerator()

    from database import db, create_db
    db.init_app(app)

    with app.app_context():
        create_db(flush=True)
        admin_id = uuid.uuid4().hex
        db.session.add(Account(
            id=admin_id,
            student_id='123456789',
            name='預設管理員',
            password='8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',  # admin
            permission=1
        ))
        db.session.commit()

    app.register_blueprint(auth_api)
    app.register_blueprint(account_api)
    # app.register_blueprint(message_api)
    # app.register_blueprint(admin_api)
    # app.register_blueprint(order_api)
    # app.register_blueprint(item_api)

    from models import Pool, Item, PoolItem
    from sqlalchemy import func
    @app.route('/test')
    def test():
        print(os.path.abspath('../'))
        return app.config['STORAGE_PATH'], 200
    return app
