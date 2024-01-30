"""Add prof model

Revision ID: b3f14082d10a
Revises: 05bcfd252834
Create Date: 2024-01-30 11:19:02.660491

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b3f14082d10a'
down_revision = '15cf483ac3d3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proofs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.String(), nullable=False),
    sa.Column('scammer_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['scammer_id'], ['scammers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('scammers', 'datetime_first',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.DateTime(),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('scammers', 'datetime_confirmed',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.DateTime(),
               existing_nullable=True)
    op.alter_column('scammers_reports', 'datetime_reported',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.DateTime(),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('scammers_reports', 'datetime_reviewed',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.DateTime(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('scammers_reports', 'datetime_reviewed',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=True)
    op.alter_column('scammers_reports', 'datetime_reported',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('scammers', 'datetime_confirmed',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=True)
    op.alter_column('scammers', 'datetime_first',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.drop_table('proofs')
    # ### end Alembic commands ###