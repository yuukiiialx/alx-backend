#!/usr/bin/env python3
"""
0-app.py
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    """Return a simple string as our response"""
    return render_template("0-index.html")
