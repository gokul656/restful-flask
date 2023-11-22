from flask import Flask

from web import db
from web.app.api.auth import auth_blueprints
from web.app.api.user import user_blueprints
from web.app.commons.error_handlers import exception_handler

__app = Flask(__name__)
# config DB URI
__app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"


def create_app() -> Flask:
    # registering base routes
    blueprint_wrapper_list = [auth_blueprints, user_blueprints]
    for wrapper in blueprint_wrapper_list:
        for blueprint in wrapper.get_blueprints():
            __app.register_blueprint(blueprint, url_prefix=wrapper.get_url_prefix())

    # error handlers
    __app.register_error_handler(Exception, exception_handler)

    with __app.app_context():
        db.init_app(__app)
        db.create_all()

    return __app
