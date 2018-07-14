#!/usr/bin/env bash

PROJECT_ROOT=$(dirname $(cd `dirname $0`; pwd))
DATA_DIR=${PROJECT_ROOT}/pgsql/data
USER=${1:-luoo}
DB_NAME=${2:-luoo}
PORT=${3:-54321}
DB_HOST=${4:-localhost}

pg_ctl start -D ${DATA_DIR} -o "-p ${PORT}" -l ${DATA_DIR}/postgresql.log
