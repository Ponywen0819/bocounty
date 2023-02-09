from flask import Flask, render_template, make_response, Blueprint
from flasgger import Swagger

from Enums.FlaskConfigEnum import FlaskConfigEnum

from modules.configs import Configure
from modules.jwt_util import JWTGenerator
from modules.crypto_utils import CryptoUtils

app = Flask(__name__)

if __name__ == "__main__":
    app.config[FlaskConfigEnum.AppConfig] = Configure()
    app.config[FlaskConfigEnum.JWTGenerator] = JWTGenerator(app.config[FlaskConfigEnum.AppConfig])
    app.config[FlaskConfigEnum.Crypto] = CryptoUtils(app.config[FlaskConfigEnum.AppConfig])

    from apps import auth
    app.register_blueprint(auth.app, url_prefix='/account')

    app.run(host="0.0.0.0", debug=True)
