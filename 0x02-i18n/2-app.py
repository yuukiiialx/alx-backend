#!/usr/bin/env python3
"""
2-app.py
"""

from flask import Flask, render_template
from flask_babel import Babel
from flask import request


class Config(object):
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)


app.config.from_object(Config)


def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale from request"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello_world() -> str:
    """Return a simple string as our response"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
