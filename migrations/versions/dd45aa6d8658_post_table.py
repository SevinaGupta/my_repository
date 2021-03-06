"""post table

Revision ID: dd45aa6d8658
Revises: bd2fc65f4c5e
Create Date: 2020-03-09 14:37:12.686657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd45aa6d8658'
down_revision = 'bd2fc65f4c5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_created_on'), 'post', ['created_on'], unique=False)
    op.create_index(op.f('ix_user_created_on'), 'user', ['created_on'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_created_on'), table_name='user')
    op.drop_index(op.f('ix_post_created_on'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
