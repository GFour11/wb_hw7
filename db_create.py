from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

class Results(Base):
    __tablename__ ='results'
    id = Column(Integer, primary_key=True)
    result = Column(Integer, nullable=False)
    date_of = Column('date_of', Date, nullable=False)
    student_id = Column('student_id', ForeignKey("students.id",ondelete="CASCADE"))
    subject_id =Column( 'subject_id', ForeignKey("subjects.id", ondelete="CASCADE"))
    student = relationship('Students', backref='result' )
    subject =relationship('Subjects', backref='result' )

class GroupNumber(Base):
    __tablename__ = 'group_number'
    id = Column(Integer, primary_key=True)
    group_number = Column(String(10), unique=True)


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name_surname = Column(String(50), unique=True, nullable=False)
    group_number = Column(String(10), ForeignKey('group_number.id'))
    group = relationship(GroupNumber, backref='students')


class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    teacher = Column(String(10), unique=True)


class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject = Column(String(50), unique=True, nullable=False)
    teacher_id = Column(String(10), ForeignKey('teachers.id'))
    teachers = relationship(Teachers)
