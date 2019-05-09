from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

class Items(Base):
    """
    Items table
    """
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    quantity = Column(Integer)
    description = Column(String(256))
    date_added = Column(DateTime())

#    a=  'INSERT INTO items %s (name, quantity, description, date_added) VALUES (%s,%s, %s, %s, %s)', (1,'hi', 4, 'no', 2019-05-12)
# a= INSERT INTO items %s (name, quantity, description, date_added) VALUES (%s, %s, %s, %s), ('hi', 4, 'no', 2019-05-12)

# cur.execute('INSERT INTO %s (name, quantity, description) VALUES (%s, %s, %s)', ('hi', 4, 'no'))

#conn = psycopg2.connect("dbname='flaskapp_db' user='docker_pg' host='localhost' password='helloworld' port='5432'")