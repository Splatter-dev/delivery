from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask


def init_app(app: Flask):
    DebugToolbarExtension(app)
