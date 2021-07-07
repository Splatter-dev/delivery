from flask import Flask

from delivery.extensions import site
from delivery.extensions import toolbar
from delivery.extensions import config


def create_app():
    app = Flask(__name__)
    # app.register_blueprint(blueprint=bp)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)  # uma forma mais organizada de fazer o registro do blueprint
    return app
