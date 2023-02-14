from flask import Flask, render_template, make_response, Blueprint
from flasgger import Swagger

from Enums.FlaskConfigEnum import FlaskConfigEnum as CEunm

from modules.configs import Configure
from modules.jwt_util import JWTGenerator
from modules.crypto_utils import CryptoUtils

from apps import auth
app = Flask(__name__)
app.register_blueprint(auth.auth, url_prefix='/account')

if __name__ == "__main__":
    # app.config[CEunm.AppConfig] = Configure()
    # app.config[CEunm.JWTGenerator] = JWTGenerator(app.config[CEunm.AppConfig])
    # app.config[CEunm.Crypto] = CryptoUtils(app.config[CEunm.AppConfig])

    configSetting = Configure()
    for setting in CEunm:
        app.config[setting] = configSetting[setting]

    app.run(host="0.0.0.0", debug=True)
