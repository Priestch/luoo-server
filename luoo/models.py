from playhouse.postgres_ext import *

from luoo import flask_app


class BaseModel(Model):
    class Meta:
        database = flask_app.db.database
        legacy_table_names = False


class Volume(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    description = ArrayField(TextField)
    vol_number = CharField(max_length=255)
    author_id = IntegerField(null=False)
    prev = IntegerField(null=False)
    next = IntegerField(null=True)
    cover = CharField(max_length=600)
    created_at = DateTimeField()


class SimilarVolume(BaseModel):
    query = ForeignKeyField(Volume)
    refer = ForeignKeyField(Volume)


class VolumeAuthor(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    avatar = CharField(max_length=255)


class Tag(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    alias = CharField(max_length=255)


class VolumeTag(BaseModel):
    volume = ForeignKeyField(Volume, backref="tags")
    tag = ForeignKeyField(Tag, backref="volumes")
