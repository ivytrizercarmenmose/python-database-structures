# install peewee
from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "carmen.db"))


# creating a table
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)


class Student(Model):
    student_name = CharField()
    student_ID = CharField(unique=True)
    student_class = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)
