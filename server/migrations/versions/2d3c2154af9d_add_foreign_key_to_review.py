from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1aac1728bc8e'
down_revision = '03b23eea86d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### Batch mode for SQLite compatibility ###
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_reviews_employee_id_employees',
            'employees',
            ['employee_id'],
            ['id']
        )


def downgrade():
    # ### Batch mode for SQLite compatibility ###
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')
