# -*- coding: utf-8 -*-
from flask import render_template

from . import flask_app


@flask_app.route("/")
def hello_world():
    return render_template("index.html")
