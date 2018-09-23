#!/usr/bin/env bash

PROJECT_ROOT=$(dirname $(cd `dirname $0`; pwd))
PROJECT_STATIC=${PROJECT_ROOT}/luoo/static
PROJECT_TEMPLATES=${PROJECT_ROOT}/luoo/templates


FRONTEND_DIST=~/Enter/luoo-pwa/dist/
echo ${FRONTEND_DIST};

echo "clean static..."
rm -rf ${PROJECT_STATIC}/*
echo ""


echo "copy index.html"
cp ${FRONTEND_DIST}/index.html ${PROJECT_TEMPLATES}

echo "copy static assets..."
cp -r ${FRONTEND_DIST}/css ${PROJECT_STATIC}
cp -r ${FRONTEND_DIST}/img ${PROJECT_STATIC}
cp -r ${FRONTEND_DIST}/js ${PROJECT_STATIC}
cp ${FRONTEND_DIST}/*.js ${PROJECT_STATIC}
cp ${FRONTEND_DIST}/*.json ${PROJECT_STATIC}
cp ${FRONTEND_DIST}/favicon.ico ${PROJECT_STATIC}

