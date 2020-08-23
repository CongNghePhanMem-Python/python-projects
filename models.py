from flask import json
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Float, CheckConstraint
from sqlalchemy.orm import relationship
from QLHS import db, admin
from flask_login import UserMixin


class User (db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

    def __str__(self):
        return self.name




class Grades(db.Model):
    __table_name__ = "grades"
    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    grade_name = Column(String(50), unique=True)
    classes = relationship('Classes', backref='grade', lazy=True)

    def __str__(self):
        return self.grade_name


class Classes(db.Model):
    __table_name__ = "class"
    class_id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(50), unique=True)
    total_students = Column(Integer)
    students = relationship('Students', backref='classes', lazy=True)
    grade_id = Column(Integer, ForeignKey('grades.grade_id'), nullable=False)

    def __str__(self):
        return str(self.grade.grade_name) + self.class_name


class Semesters(db.Model):
    semester_id = Column(Integer, primary_key=True, autoincrement=True)
    semester_name = Column(String(50))
    students = relationship('Students', backref='semester', lazy=True)

    def __str__(self):
        return self.semester_name


class Gender(db.Model):
    gender_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    gender_name = Column(String(50))
    students = relationship('Students', backref='gender', lazy=True)

    def __str__(self):
        return self.gender_name


class Students(db.Model):
    __table_name__ = "student"
    student_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    student_name = Column(String(50), nullable=False)
    gender_id = Column(Integer, ForeignKey(Gender.gender_id), nullable=False)
    birthday = Column(DateTime)
    address = Column(String(1500))
    email = Column(String(1500), unique=True)
    class_id = Column(Integer, ForeignKey(Classes.class_id))
    marks = relationship('Marks', backref='student', lazy=True)
    semester_id = Column(Integer, ForeignKey(Semesters.semester_id), nullable=False)

    def __str__(self):
        return self.student_name


class Subjects(db.Model):
    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(50))
    coefficient = Column(db.Float)
    mark = relationship('Marks', backref='subject', lazy=True)

    def __str__(self):
        return self.subject_name


class Marks(db.Model):
    subject_id = Column(Integer, ForeignKey(Subjects.subject_id), primary_key=True)
    student_id = Column(Integer, ForeignKey(Students.student_id), primary_key=True, default=0)
    mark_1 = Column(Float)
    mark_2 = Column(Float)
    mark_3 = Column(Float)
    mark_semester = Column(Float)
    mark_total = Column(Float)
    gpa = relationship('Gpas', backref='mark', lazy=True)

    def __repr__(self):
        return self.subject.subject_name + ": " + str(self.mark_total) + ", " + self.student.student_name


class Gpas(db.Model):
    gpa_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    student_id = Column(Integer, ForeignKey(Marks.student_id))
    mark_gpa = Column(Float)

    def __str__(self):
        return str(self.mark_gpa)


if __name__ == "__main__":
    db.create_all()
