#!/usr/bin/env bash

export FLASK_APP=luoo
export FLASK_ENV=development

celery -A luoo.celery worker -l info
