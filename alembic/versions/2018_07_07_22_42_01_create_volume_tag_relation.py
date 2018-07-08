"""create volume tag relation

Revision ID: 6489cfa9211e
Revises: 4d5863eece2c
Create Date: 2018-07-07 22:42:01.856987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6489cfa9211e"
down_revision = "4d5863eece2c"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "volume_tag",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("volume_id", sa.Integer),
        sa.Column("tag_id", sa.Integer),
    )


def downgrade():
    op.drop_table("volume_tag")
