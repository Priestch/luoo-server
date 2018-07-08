"""create volume tag

Revision ID: 4d5863eece2c
Revises: a80d25a8080e
Create Date: 2018-07-07 22:40:21.910682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4d5863eece2c"
down_revision = "a80d25a8080e"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tag",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=255)),
        sa.Column("alias", sa.String(length=255)),
    )

    op.create_unique_constraint("uq_tag_alias", "tag", ["alias"])


def downgrade():
    op.drop_constraint("uq_tag_alias", "tag")
    op.drop_table("tag")
