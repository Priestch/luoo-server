from flask import jsonify, abort


def error(errors, status_code=400):
    return abort(status_code, response=jsonify(errors))


def success(data, status_code=200):
    return jsonify(data), status_code
