import os
import secrets
from utils.jwt_util import JWTGenerator
from datetime import timedelta
from urllib.parse import quote

SECRET_KEY: bytes = os.urandom(24)
SQLALCHEMY_DATABASE_URI: str = "sqlite:///" + os.path.join(os.path.abspath("../"), "bocountry.sqlite")
STORAGE_PATH: str = os.path.join(os.path.abspath("../"), "storage")

