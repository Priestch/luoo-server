# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify

# from flask_restful import Api

# from luoo.resources import SongResource

bp = Blueprint("api", __name__)
# api = Api(api_bp)

# api.add_resource(SongResource, "/songs/<int:song_id>")


@bp.route("/songs/<song_id>")
def get_song(song_id):
    return jsonify({"id": song_id, "name": "test name"})


# @bp.route("/volumes/<volume_id>")
# def get_song(volume_id):
#     return jsonify({"id": volume_id, "name": "test name"})
