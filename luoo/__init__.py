import os
from subprocess import call

import click
from flask import Flask
from flask.cli import AppGroup
from flask_peewee.db import Database

from luoo import config
from luoo.blueprints.api import bp


def configure_app_by_env(app):
    flask_env = os.environ.get("FLASK_ENV")
    app.config.from_pyfile("{}.py".format(flask_env))


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    configure_app_by_env(app)
    app.db = Database(app)

    app.register_blueprint(bp, url_prefix="/api")

    return app


flask_app = create_app()

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
