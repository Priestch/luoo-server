from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from luoo.constants import LUOO_CDN_BASE, LUOO_VOLUME_PIC_PREFIX, LUOO_VOLUME_PIC_SUFFIX

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

volume_tag = db.Table(
    "volume_tag",
    db.metadata,
    db.Column("volume_id", db.Integer, db.ForeignKey("volume.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)


class Volume(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.Text)
    description = db.Column(db.ARRAY(db.Text))
    vol_number = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("volume_author.id"), nullable=False)
    prev = db.Column(db.Integer, nullable=False)
    next = db.Column(db.Integer, nullable=False)
    cover = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    tags = db.relationship("Tag", secondary=volume_tag, backref="volumes")
    author = db.relationship("VolumeAuthor", uselist=False)

    @property
    def cover_url(self):
        return "{}{}{}{}".format(
            LUOO_CDN_BASE, LUOO_VOLUME_PIC_PREFIX, self.cover, LUOO_VOLUME_PIC_SUFFIX
        )


# class SimilarVolume(db.Model):
#     query = ForeignKeyField(Volume)
#     refer = ForeignKeyField(Volume)


class VolumeAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.Text, nullable=False)
    avatar = db.Column(db.Text)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    alias = db.Column(db.Text, nullable=False)
