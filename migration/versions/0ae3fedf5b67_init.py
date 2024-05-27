"""Init

Revision ID: 0ae3fedf5b67
Revises: 
Create Date: 2024-05-27 22:52:06.614014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '0ae3fedf5b67'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=False),
    sa.Column('last_name', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('phone_number', sa.String(length=30), nullable=False),
    sa.Column('birthday', sa.String(length=30), nullable=False),
    sa.Column('data', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_last_name'), 'contacts', ['last_name'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_contacts_last_name'), table_name='contacts')
    op.drop_table('contacts')
    op.drop_table('users')
