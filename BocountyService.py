from flask import Flask, render_template, make_response, Blueprint
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy

from Enums.FlaskConfigEnum import FlaskConfigEnum as ConfigEnum

from modules.configs import Configure
from modules.module_factory import ModuleFactory

from apps import auth_api

app = Flask(__name__)

configSetting = Configure()
for name, val in configSetting.items():
    app.config[name] = val
app.config[ConfigEnum.Factory] = ModuleFactory(app.config)

app.register_blueprint(auth_api.auth, url_prefix='/account')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
