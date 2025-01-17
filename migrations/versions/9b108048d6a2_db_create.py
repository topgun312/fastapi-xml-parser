"""DB create

Revision ID: 9b108048d6a2
Revises: 
Create Date: 2024-11-23 13:06:40.449507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b108048d6a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prompt_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('total_revenue', sa.Float(), nullable=True),
    sa.Column('top_product', sa.String(), nullable=True),
    sa.Column('top_category', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_prompt_table_id'), 'prompt_table', ['id'], unique=False)
    op.create_table('sale_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sale_date', sa.String(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sale_table_id'), 'sale_table', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sale_table_id'), table_name='sale_table')
    op.drop_table('sale_table')
    op.drop_index(op.f('ix_prompt_table_id'), table_name='prompt_table')
    op.drop_table('prompt_table')
    # ### end Alembic commands ###
