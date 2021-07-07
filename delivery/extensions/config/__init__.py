from flask import Flask


def init_app(app: Flask):
    app.config["SECRET_KEY"] = "12345"
    app.config["FLASK_APP"] = "delivery/app.py"
    app.config["FLASK_ENV"] = "development"

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True