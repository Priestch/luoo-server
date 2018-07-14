#!/usr/bin/env bash

FLASK_APP=luoo
FLASK_ENV=development

celery -A luoo.celery worker -l info
