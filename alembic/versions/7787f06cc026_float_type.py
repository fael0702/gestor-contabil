"""float_type

Revision ID: 7787f06cc026
Revises: e447a0bf6a87
Create Date: 2024-04-02 01:21:18.585186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7787f06cc026'
down_revision: Union[str, None] = 'e447a0bf6a87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('expenses', 'valor',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    op.alter_column('revenues', 'valor',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('revenues', 'valor',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('expenses', 'valor',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###