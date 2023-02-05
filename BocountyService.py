from flask import Flask, render_template, make_response, Blueprint
from flasgger import Swagger

from Enums.FlaskConfigEnum import FlaskConfigEnum

from apps import auth

from modules.configs import Configure
from modules.jwt_util import JWTGenerator


app = Flask(__name__)
app.register_blueprint(auth.app, url_prefix='/account')


if __name__ == "__main__":

    app.config[FlaskConfigEnum.AppConfig] = Configure()
    app.config[FlaskConfigEnum.JWTGenerator] = JWTGenerator(app.config['config'])
    # app.config['crypto'] = crypto_utils(app.config['config'])

    app.run(host="0.0.0.0", debug=True)
