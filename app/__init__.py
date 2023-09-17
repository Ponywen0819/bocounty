from flask import Flask


def create_app(config_filename=None):
    main = Flask(__name__, template_folder='./template', static_folder='./public')
    if config_filename is None:
        main.config.from_pyfile('config.py')
    else:
        main.config.from_pyfile(config_filename)

    register_blueprints(main)

    return main


def register_blueprints(app: Flask):
    from app.api.auth import auth_api
    app.register_blueprint(auth_api)

    from app.api.user import user_api
    app.register_blueprint(user_api)

    from app.api.order import order_api
    app.register_blueprint(order_api)

    from app.api.report.route import report_api
    app.register_blueprint(report_api)

    from app.api.chatroom.route import chatroom_api
    app.register_blueprint(chatroom_api)
