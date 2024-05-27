"""add veryfi

Revision ID: c5ce3c4e5404
Revises: 35a919d34126
Create Date: 2024-05-27 15:25:21.910090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'c5ce3c4e5404'
down_revision: Union[str, None] = '35a919d34126'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'confirmed')
