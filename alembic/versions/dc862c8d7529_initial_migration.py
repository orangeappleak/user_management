"""initial migration

Revision ID: dc862c8d7529
Revises: 208a4d4c3df8
Create Date: 2024-05-05 04:35:16.072970

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc862c8d7529'
down_revision: Union[str, None] = '208a4d4c3df8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events', 'created_by',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events', 'created_by',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###
