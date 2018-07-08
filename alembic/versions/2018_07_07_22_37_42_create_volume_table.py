"""create volume table

Revision ID: e1c12754a538
Revises:
Create Date: 2018-07-07 22:37:42.310077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e1c12754a538"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "volume",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=False),
        sa.Column("name", sa.String(length=255)),
        sa.Column("description", sa.ARRAY(sa.String)),
        sa.Column("vol_number", sa.String(length=255)),
        sa.Column("author_id", sa.Integer),
        sa.Column("prev", sa.Integer),
        sa.Column("next", sa.Integer),
        sa.Column("cover", sa.String(length=600)),
        sa.Column("created_at", sa.DateTime),
    )

    op.create_index("ik_volume_author_id", "volume", ["author_id"])


def downgrade():
    op.drop_index("ik_volume_author_id", "volume")
    op.drop_table("volume")
