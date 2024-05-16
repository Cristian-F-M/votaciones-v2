"""Seed data

Revision ID: 2c34380c4741
Revises: 6d7af8d501dc
Create Date: 2024-05-16 12:24:18.140488

"""
from alembic import op
import sqlalchemy as sa
from app.utils.seed import seed_database

# revision identifiers, used by Alembic.
revision = '2c34380c4741'
down_revision = '6d7af8d501dc'
branch_labels = None
depends_on = None


def upgrade():
    seed_database()


def downgrade():
    pass
