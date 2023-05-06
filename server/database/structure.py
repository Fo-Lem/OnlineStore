from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, Text, ForeignKey, Double

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/woodhouse")
data = MetaData()

heroes = Table('heroes', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('name', Text, nullable=False)
)

categories = Table('categories', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('name', Text, nullable=False)
)

product_type = Table('product_type', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('name', Text, nullable=False)
)

clients = Table('clients', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('phone', Text, nullable=False),
    Column('description', Text, nullable=False)
)

identity = Table('identity', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('name', Text, nullable=False),
    Column('hero_id', ForeignKey('heroes.id')),
    Column('product_type_id', ForeignKey('product_type.id')),
    Column('category_id', ForeignKey('categories.id')),
    Column('description', Text, nullable=False)
)

items = Table('item', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('identity_id', ForeignKey('identity.id')),
    Column('size', Text, nullable=False),
    Column('price', Double, nullable=False)
)

sel = items.select()
conn = engine.connect()
res = conn.execute(sel)

for row in res:
    print(row)