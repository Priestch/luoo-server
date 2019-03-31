import os
from subprocess import call

import click
from flask import Flask
from flask.cli import AppGroup

from luoo import config
from luoo.celery import make_celery
from luoo.models import db


def configure_app_by_env(app):
    flask_env = os.environ.get("FLASK_ENV")
    app.config.from_pyfile("{}.py".format(flask_env))


def handle_non_exist_request(e):
    return "Page not Found!", 404


def register_error_handler(app):
    app.register_error_handler(404, handle_non_exist_request)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    configure_app_by_env(app)

    db.init_app(app)

    register_error_handler(app)

    return app


def register_blueprints():
    from luoo.api import api_bp
    from luoo.views import views

    flask_app.register_blueprint(api_bp, url_prefix="/api")
    flask_app.register_blueprint(views, url_prefix="/")


flask_app = create_app()
celery = make_celery(flask_app)
register_blueprints()

db_cli = AppGroup("db")
crawler_cli = AppGroup("crawler")


@db_cli.command("upgrade")
@click.option("--revision", "-r", default="head", help="revision upgrade to")
def upgrade(revision):
    cmdline = ["alembic", "-c", "instance/alembic.ini", "upgrade", revision]
    call(cmdline)


@db_cli.command("downgrade")
@click.option("--revision", "-r", default="base", help="revision downgrade to")
def upgrade(revision):
    cmdline = ["alembic", "-c", "instance/alembic.ini", "downgrade", revision]
    call(cmdline)


@db_cli.command("run")
@click.option("--volume", "-v", default="base", help="revision downgrade to")
def upgrade(revision):
    cmdline = ["alembic", "-c", "instance/alembic.ini", "downgrade", revision]
    call(cmdline)


flask_app.cli.add_command(db_cli)
flask_app.cli.add_command(crawler_cli)

from . import views
