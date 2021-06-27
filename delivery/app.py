from flask import Flask, render_template, request
from delivery.extensions import site


def create_app():
    app = Flask(__name__)
    # app.register_blueprint(blueprint=bp)
    site.init_app(app) # uma forma mais organizada de fazer o registro do blueprint
    return app
