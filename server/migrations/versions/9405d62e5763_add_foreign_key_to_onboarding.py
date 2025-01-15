"""add foreign key to onboarding

Revision ID: 9405d62e5763
Revises: 1aac1728bc8e
Create Date: 2025-01-15 13:26:10.339478
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Integer, String, DateTime, Boolean

# revision identifiers, used by Alembic.
revision = '9405d62e5763'
down_revision = '1aac1728bc8e'
branch_labels = None
depends_on = None


def upgrade():
    # Start batch mode to handle SQLite limitations
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            op.f('fk_onboardings_employee_id_employees'), 
            'employees', ['employee_id'], ['id']
        )


def downgrade():
    # Start batch mode for the downgrade as well
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')
