import sqlite3
from os import getcwd, path
from flask import g, appcontext_tearing_down

DB_PATH = path.join(getcwd(), 'bocountry.sqlite')


def get_db() -> sqlite3.Connection:
    db: sqlite3.Connection = g.setdefault("_database", sqlite3.connect(DB_PATH))
    return db


def disconnect(sender, **extra):
    db: sqlite3.Connection = g.setdefault("_database", sqlite3.connect(DB_PATH))
    db.close()


appcontext_tearing_down.connect(disconnect)

from .get import get
from .create import create
from .delete import delete
from .update import update
