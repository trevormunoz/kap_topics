"""create topic table

Revision ID: 541089720fcb
Revises: None
Create Date: 2013-12-06 09:05:36.856257

"""

# revision identifiers, used by Alembic.
revision = '541089720fcb'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'topic',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('orig_label', sa.String(80), nullable=False),
        sa.Column('supplied_label', sa.String(80)),
        sa.Column('terms_top', sa.Text),
        sa.Column('terms_all', sa.Text)
    )


def downgrade():
    op.drop_table('topic')
