"""added onupdate and ondelete on tables

Revision ID: 9953f5a313e2
Revises: 0242fe927739
Create Date: 2021-04-14 13:02:39.415477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9953f5a313e2'
down_revision = '0242fe927739'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('barbers_barber_shop_id_fkey', 'barbers', type_='foreignkey')
    op.create_foreign_key(None, 'barbers', 'barber_shop', ['barber_shop_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('services_barber_id_fkey', 'services', type_='foreignkey')
    op.create_foreign_key(None, 'services', 'barbers', ['barber_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'services', type_='foreignkey')
    op.create_foreign_key('services_barber_id_fkey', 'services', 'barbers', ['barber_id'], ['id'])
    op.drop_constraint(None, 'barbers', type_='foreignkey')
    op.create_foreign_key('barbers_barber_shop_id_fkey', 'barbers', 'barber_shop', ['barber_shop_id'], ['id'])
    # ### end Alembic commands ###