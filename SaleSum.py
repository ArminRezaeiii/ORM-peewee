from peewee import *


db = SqliteDatabase('sales.db')


class BaseModel(Model):
    class Meta:
        database = db


class Sales(BaseModel):
    product = CharField()
    quantity = IntegerField()


def setup_database():
    db.connect()
    db.create_tables([Sales])


    Sales.delete().execute()


    Sales.create(product='Laptop', quantity=5)
    Sales.create(product='Phone', quantity=3)
    Sales.create(product='Laptop', quantity=2)
    Sales.create(product='Tablet', quantity=4)
    Sales.create(product='Phone', quantity=7)


def calculate_sales_summary():
    query = (Sales
             .select(Sales.product, fn.SUM(Sales.quantity).alias('total_quantity'))
             .group_by(Sales.product))

    print("مجموع فروش هر محصول:")
    for item in query:
        print(f"{item.product}: {item.total_quantity}")

if __name__ == '__main__':
    setup_database()
    calculate_sales_summary()
