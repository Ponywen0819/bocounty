from flask import Flask


def create_app(config_filename=None):
    main = Flask(__name__, template_folder='./template', static_folder='./src')
    if config_filename is None:
        main.config.from_pyfile('config.py')
    else:
        main.config.from_pyfile(config_filename)
    from app.utils.setting_util import SettingUtil
    setter = SettingUtil(main.config)
    main.config["setting"] = setter.load_setting()
    main.config["verify_code"] = {}

    from app.utils.jwt_util import JWTGenerator
    main.config['jwt_gen']: JWTGenerator = JWTGenerator()

    from app.database import db, create_db
    db.init_app(main)

    register_blueprints(main)

    return main


def register_blueprints(app: Flask):
    from app.api.user import user_api
    app.register_blueprint(user_api)

    from app.api.auth import auth_api
    app.register_blueprint(auth_api)
