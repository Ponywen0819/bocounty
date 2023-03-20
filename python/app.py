import secrets
import uuid
from utils.jwt_util import JWTGenerator
from flask import Flask
from api.auth import auth_api
from api.account import account_api
from models import Account, PickedItem


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
        db.session.add(PickedItem(
            user_id=admin_id
        ))
        db.session.commit()

    app.register_blueprint(auth_api)
    app.register_blueprint(account_api)

    return app
