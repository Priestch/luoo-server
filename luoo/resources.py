# -*- coding: utf-8 -*-

from flask_restful import Resource, marshal_with
from flask_restful import fields

from .models import Song

song_fields = {"id": fields.Integer, "title": fields.String, "url": fields.String}


class SongResource(Resource):
    @marshal_with(song_fields)
    def get(self, song_id):
        return Song.query.get(song_id)
