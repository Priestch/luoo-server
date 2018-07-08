"""create volume author table

Revision ID: a80d25a8080e
Revises: e1c12754a538
Create Date: 2018-07-07 22:39:34.598715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a80d25a8080e"
down_revision = "e1c12754a538"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "volume_author",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=False),
        sa.Column("name", sa.String(length=255)),
        sa.Column("avatar", sa.String(length=255)),
    )


def downgrade():
    op.drop_table("volume_author")
