from random import randint
from faker import Faker
from datetime import datetime, date, timedelta
from connect_db import session
from db_create import Teachers, Subjects, Students, Results, GroupNumber
fake = Faker('uk-UA')


subjects = ['PE','Physic', 'Chemistry', 'Law','Journalistic']
groups=['F-11', 'K34-13','AA-58']


def seed_teachers():
    teachers = [fake.name() for _ in range(1,6)]
    for teacher in teachers:
        teach =Teachers(teacher = teacher)
        session.add(teach)
    session.commit()

def seed_group():
    for group in groups:
        gr = GroupNumber(group_number = group)
        session.add(gr)
    session.commit()


def seed_students():
    for student in range(31):
        name = fake.name()
        group_id = randint(1, len(groups))
        res = Students(name_surname = name, group_number=group_id )
        session.add(res)
    session.commit()

def seed_subjects():
    for sub in subjects:
        res = Subjects(subject = sub, teacher_id = randint(1,6))
        session.add(res)
    session.commit()


def seed_results():
    start_studying = datetime.strptime('2022-09-01','%Y-%m-%d')
    finish_studying = datetime.strptime('2023-06-30', '%Y-%m-%d')

    def get_date(start_studying, finish_studying):
        result=[]
        start: date = start_studying
        while start<finish_studying:
            if start.isoweekday()<6:
                result.append(start)
            start+=timedelta(1)
        return result

    dates=get_date(start_studying,finish_studying)
    for day in dates:
        res = Results(student_id = randint(1,31), subject_id = randint(1,6), result =randint(1,12), date_of = day)
        session.add(res)
    session.commit()

if __name__ == '__main__':
    seed_teachers()
    seed_group()
    seed_students()
    seed_subjects()
    seed_results()
    session.close()