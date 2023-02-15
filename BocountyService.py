from flask import Flask, render_template, make_response, Blueprint
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

import apps.auth_api
from Enums.FlaskConfigEnum import FlaskConfigEnum as ConfigEnum

from modules.configs import Configure
from modules.module_factory import ModuleFactory

from apps.auth_api import auth
from apps.account_manage import account

app = Flask(__name__)

configSetting = Configure()
for name, val in configSetting.items():
    app.config[name] = val
app.config[ConfigEnum.Factory] = ModuleFactory(app.config)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(account, url_prefix='/account')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
