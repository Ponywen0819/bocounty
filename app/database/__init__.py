import uuid

from flask import current_app
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def check_db():
    full_file_path = os.path.join(os.getcwd(), 'bocountry.sqlite')
    print(full_file_path, os.path.exists(full_file_path))
    return os.path.exists(full_file_path)


def create_default_admin(student_id="123456789", name="預設管理員"):
    from app.models import Account

    admin_exsit = Account.query.filter(
        Account.student_id == student_id).count()
    if admin_exsit:
        return
    admin_id = uuid.uuid4().hex
    db.session.add(Account(
        id=admin_id,
        student_id=student_id,
        name=name,
        password='8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',  # admin
        permission=1,
        bocoin=1000
    ))
    db.session.commit()


def create_db(flush=False):
    with current_app.app_context():
        if flush:
            db.drop_all()
        db.create_all()
        create_default_admin()
