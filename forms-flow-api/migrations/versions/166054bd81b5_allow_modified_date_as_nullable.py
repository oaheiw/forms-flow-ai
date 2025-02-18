"""allow modified date as nullable

Revision ID: 166054bd81b5
Revises: 80b8d5e95e9b
Create Date: 2021-10-11 03:47:20.983464

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "166054bd81b5"
down_revision = "80b8d5e95e9b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "application", "modified", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
    op.alter_column(
        "form_process_mapper",
        "modified",
        existing_type=postgresql.TIMESTAMP(),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "form_process_mapper",
        "modified",
        existing_type=postgresql.TIMESTAMP(),
        nullable=False,
    )
    op.alter_column(
        "application", "modified", existing_type=postgresql.TIMESTAMP(), nullable=False
    )
    # ### end Alembic commands ###
