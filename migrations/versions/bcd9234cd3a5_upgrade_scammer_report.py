"""upgrade scammer report

Revision ID: bcd9234cd3a5
Revises: 6515bd92c276
Create Date: 2023-11-23 11:37:41.474500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcd9234cd3a5'
down_revision = '6515bd92c276'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('scammers_reports', sa.Column('text', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('scammers_reports', 'text')
    # ### end Alembic commands ###
