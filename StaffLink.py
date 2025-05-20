from peewee import *

db = SqliteDatabase('company.db')


class BaseModel(Model):
    class Meta:
        database = db


class Department(BaseModel):
    name = CharField()


class Employee(BaseModel):
    name = CharField()
    department = ForeignKeyField(Department, backref='employees')


db.connect()
db.create_tables([Department, Employee])


if Department.select().count() == 0:

    dep1 = Department.create(name='منابع انسانی')
    dep2 = Department.create(name='فناوری اطلاعات')
    dep3 = Department.create(name='مالی')


    Employee.create(name='علی رضایی', department=dep1)
    Employee.create(name='مینا مرادی', department=dep2)
    Employee.create(name='حسین احمدی', department=dep3)
    Employee.create(name='سارا محمدی', department=dep2)


query = Employee.select(Employee.name, Department.name).join(Department)


print("لیست کارکنان و دپارتمان‌هایشان:")
for employee in query:
    print(f"{employee.name} - {employee.department.name}")
