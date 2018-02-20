"""works table

Revision ID: 504903e03612
Revises: 
Create Date: 2018-02-20 09:51:40.764943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '504903e03612'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('work',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('body', sa.String(length=255), nullable=True),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('work')
    # ### end Alembic commands ###