from pprint import pprint
from db_create import Teachers, Subjects, Students, Results, GroupNumber
from sqlalchemy import func, desc, and_, select
from connect_db import session


def select_1():
    res = session.query(Students.name_surname, func.avg(Results.result).label('avg_result'))\
    .select_from(Results).join(Students).group_by(Students.id).order_by(desc('avg_result')).limit(5).all()
    return res


def select_2():
    res = session.query(Students.name_surname, func.avg(Results.result).label('avg_result'))\
    .select_from(Results).join(Students).join(Subjects).filter(Subjects.id == 1).group_by(Students.id).order_by(desc('avg_result')).limit(1).all()
    return res


def select_3():
    res = session.query(GroupNumber.group_number, func.avg(Results.result).label('avg_result'))\
    .select_from(Results).join(Students).join(Subjects).join(GroupNumber).filter(Students.id == 1).\
        group_by(GroupNumber.group_number).order_by(desc('avg_result')).all()
    return res


def select_4():
    res = session.query(GroupNumber.group_number, func.avg(Results.result).label('avg_result'))\
    .select_from(Results).join(Students).join(GroupNumber).group_by(GroupNumber.group_number).order_by(desc('avg_result')).all()
    return res


def select_5():
    res = session.query(Teachers.teacher, Subjects.subject).select_from(Subjects).join(Teachers).filter(Teachers.id ==1).all()
    return res


def select_6():
    res = session.query(Students.name_surname, Students.group_number).select_from(GroupNumber).join(Students)\
        .filter(GroupNumber.id ==1).group_by(GroupNumber.group_number).limit(1).all()
    return res


def select_7():
    res=session.query(GroupNumber.group_number, Subjects.subject, Students.name_surname, func.avg(Results.result)\
                      .label('avg_result'))\
    .select_from(Results).join(Students).join(Subjects).join(GroupNumber).filter(and_(GroupNumber.id ==1,Subjects.id ==2))\
    .group_by(Students.id).order_by(desc('avg_result')).all()
    return res


def select_8():
    res = session.query(Teachers.teacher, Subjects.subject, func.avg(Results.result)\
                      .label('avg_result'))\
    .select_from(Results).join(Subjects).join(Teachers).filter(Teachers.id == 1).group_by(Subjects.subject).all()
    return res


def select_9():
    res = session.query(Students.name_surname, Subjects.subject).select_from(Results).join(Students).join(Subjects)\
    .filter(Students.id == 4).group_by(Subjects.subject).limit(5).all()
    return res


def select_10():
    res = session.query(Subjects.subject).select_from(Results).join(Students).join(Subjects).join(Teachers)\
        .filter(and_(Students.id ==27, Teachers.id ==4)).group_by(Subjects.subject).all()
    return res
