import uuid

from flask import current_app
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def check_db():
    full_file_path = os.path.join(os.getcwd(), 'bocountry.sqlite')
    print(full_file_path, os.path.exists(full_file_path))
    return os.path.exists(full_file_path)


def create_db(flush=False):
    if flush or (not check_db()):
        with current_app.app_context():
            if flush:
                print('flush database')
                db.drop_all()
            print('create database')
            db.create_all()


