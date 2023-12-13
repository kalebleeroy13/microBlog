"""added language to posts

Revision ID: 5cb8e30a8a85
Revises: 962dd5e1dcb6
Create Date: 2023-12-13 11:43:09.553547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cb8e30a8a85'
down_revision = '962dd5e1dcb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('followers', schema=None) as batch_op:
        batch_op.alter_column('follower_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('followed_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
        batch_op.alter_column('timestamp',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.create_index(batch_op.f('ix_post_user_id'), ['user_id'], unique=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=256),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_user_id'))
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('timestamp',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
        batch_op.drop_column('language')

    with op.batch_alter_table('followers', schema=None) as batch_op:
        batch_op.alter_column('followed_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('follower_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
