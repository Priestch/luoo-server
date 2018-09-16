# -*- coding: utf-8 -*-
from flask import jsonify

from luoo.models import Volume, Tag
from . import api_bp
from luoo.schema.volume import volume_schema, tag_schema


@api_bp.route("/volumes/<int:volume_id>")
def get_volume(volume_id):
    volume = Volume.query.get_or_404(volume_id)
    dumped = volume_schema.dump(volume)
    return jsonify(dumped)


@api_bp.route("/volumes")
def get_volumes():
    volumes = Volume.query.all()
    dumped = volume_schema.dump(volumes, many=True)
    return jsonify(dumped)


@api_bp.route("/tags")
def get_tags():
    tags = Tag.query.all()
    dumped = tag_schema.dump(tags, many=True)
    return jsonify(dumped)
