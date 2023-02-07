from flask import current_app
from enum import Enum
from modules.configs import Configure
from Enums.FlaskConfigEnum import FlaskConfigEnum
from modules.jwt_util import JWTGenerator

class ModuleFactory(Enum):
    AppConfig :Configure = current_app.config[FlaskConfigEnum.AppConfig]
    JWTGenerator :JWTGenerator= current_app.config[FlaskConfigEnum.JWTGenerator]