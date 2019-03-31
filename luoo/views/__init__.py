# -*- coding: utf-8 -*-

from flask import Blueprint

views = Blueprint("views", __name__)

from . import home
