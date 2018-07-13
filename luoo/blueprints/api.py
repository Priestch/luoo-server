# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with

from luoo.models import Volume

bp = Blueprint("api", __name__)

api = Api(bp)


volume_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.List(fields.String),
    "vol_number": fields.String,
    "author_id": fields.Integer,
    "prev": fields.Integer,
    "next": fields.Integer,
    "cover_url": fields.String,
}


class VolumeResource(Resource):
    @marshal_with(volume_fields)
    def get(self, volume_id):
        volume = Volume.query.get_or_404(volume_id)
        return volume


api.add_resource(VolumeResource, "/volumes/<int:volume_id>")
