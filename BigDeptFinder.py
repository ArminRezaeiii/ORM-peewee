from peewee import *


db = SqliteDatabase('company.db')


class BaseModel(Model):
    class Meta:
        database = db


class Department(BaseModel):
    name = CharField()
    size = IntegerField()


class Employee(BaseModel):
    name = CharField()
    department = ForeignKeyField(Department, backref='employees')


db.connect()
db.create_tables([Department, Employee])


if not Department.select().exists():
    d1 = Department.create(name='HR', size=5)
    d2 = Department.create(name='Engineering', size=15)
    d3 = Department.create(name='Marketing', size=10)

    Employee.create(name='Alice', department=d1)
    Employee.create(name='Bob', department=d2)
    Employee.create(name='Charlie', department=d2)
    Employee.create(name='Dave', department=d3)
    Employee.create(name='Eve', department=d2)


largest_department = Department.select().order_by(Department.size.desc()).limit(1)


employees_in_largest_dept = Employee.select().where(Employee.department == largest_department)


print("کارکنانی که در بزرگترین دپارتمان کار می‌کنند:")
for employee in employees_in_largest_dept:
    print(f'{employee.name} - {employee.department.name}')
