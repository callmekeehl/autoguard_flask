"""empty message

Revision ID: 6a67bbdbaea6
Revises: a71e2b891876
Create Date: 2024-06-10 09:19:10.863113

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a67bbdbaea6'
down_revision = 'a71e2b891876'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('garage', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utilisateurId', sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(None, ['utilisateurId'])
        batch_op.drop_constraint('garage_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'utilisateur', ['utilisateurId'], ['utilisateurId'])

    with op.batch_alter_table('police', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utilisateurId', sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(None, ['utilisateurId'])
        batch_op.drop_constraint('police_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'utilisateur', ['utilisateurId'], ['utilisateurId'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('police', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('police_ibfk_1', 'utilisateur', ['policeId'], ['utilisateurId'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('utilisateurId')

    with op.batch_alter_table('garage', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('garage_ibfk_1', 'utilisateur', ['garageId'], ['utilisateurId'])
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('utilisateurId')

    # ### end Alembic commands ###