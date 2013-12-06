"""Add a column

Revision ID: 1ee3c3259a37
Revises: 541089720fcb
Create Date: 2013-12-06 09:21:52.152796

"""

# revision identifiers, used by Alembic.
revision = '1ee3c3259a37'
down_revision = '541089720fcb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'topic', 
        sa.Column('timestamp', sa.DateTime)
    )


def downgrade():
    op.drop_column('topic', 'timestamp')
