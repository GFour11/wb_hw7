"""Init

Revision ID: f0057ae8cb8c
Revises: 
Create Date: 2023-06-25 14:12:56.466479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0057ae8cb8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group_number',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_number', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('group_number')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('teacher')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_surname', sa.String(length=50), nullable=False),
    sa.Column('group_number', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['group_number'], ['group_number.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name_surname')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=50), nullable=False),
    sa.Column('teacher_id', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('subject')
    )
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(), nullable=True),
    sa.Column('subject_id', sa.String(), nullable=True),
    sa.Column('result', sa.Integer(), nullable=False),
    sa.Column('date_of', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('teachers')
    op.drop_table('group_number')
    # ### end Alembic commands ###