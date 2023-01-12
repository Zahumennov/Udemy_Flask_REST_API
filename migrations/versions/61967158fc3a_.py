"""empty message

Revision ID: 61967158fc3a
Revises: abb36b930768
Create Date: 2023-01-12 20:44:38.653146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61967158fc3a'
down_revision = 'abb36b930768'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Float(precision=2),
               type_=sa.REAL(),
               existing_nullable=False)

    # ### end Alembic commands ###
