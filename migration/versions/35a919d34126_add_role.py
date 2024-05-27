"""add role

Revision ID: 35a919d34126
Revises: 0ae3fedf5b67
Create Date: 2024-05-27 22:54:14.751368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '35a919d34126'
down_revision: Union[str, None] = '0ae3fedf5b67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('role', sa.Enum('admin', 'moderator', 'user', name='role'), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'role')
