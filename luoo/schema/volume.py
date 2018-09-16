from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from luoo.models import Volume, Tag


class VolumeSchema(ModelSchema):
    class Meta:
        model = Volume

    cover = fields.Method("get_volume_cover")

    def get_volume_cover(self, obj):
        return obj.cover_url


class TagSchema(ModelSchema):
    class Meta:
        model = Tag


volume_schema = VolumeSchema()
tag_schema = TagSchema()
