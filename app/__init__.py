from flask import Flask


def create_app(config_filename=None):
    main = Flask(__name__, template_folder='./template', static_folder='../public', static_url_path="/static")
    if config_filename is None:
        main.config.from_pyfile('config.py')
    else:
        main.config.from_pyfile(config_filename)

    register_blueprints(main)

    return main


def register_blueprints(app: Flask):
    from app.api.auth import auth_api
    app.register_blueprint(auth_api)

    from app.api.user.route import user_api
    app.register_blueprint(user_api)

    from app.api.order.route import order_api
    app.register_blueprint(order_api)

    from app.api.report.route import report_api
    app.register_blueprint(report_api)

    from app.api.chatroom.route import chatroom_api
    app.register_blueprint(chatroom_api)

    from app.api.message.route import message_api
    app.register_blueprint(message_api)

    from app.api.item.route import item_api
    app.register_blueprint(item_api)

    from app.api.coupon.route import coupon_api
    app.register_blueprint(coupon_api)

    from app.api.notification.route import notification_api
    app.register_blueprint(notification_api)

    from  app.api.pool.route import pool_api
    app.register_blueprint(pool_api)

    from app.api.admin.route import admin_api
    app.register_blueprint(admin_api)


