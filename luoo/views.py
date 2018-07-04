# -*- coding: utf-8 -*-

from . import app


@app.route("/")
def hello_world():
    return "Hello World!"
