# -*- coding: utf-8 -*-

from . import flask_app


@flask_app.route("/")
def hello_world():
    return "Hello World!"
