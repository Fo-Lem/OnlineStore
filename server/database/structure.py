from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, Text, ForeignKey, Double

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/woodhouse")
data = MetaData()
conn = engine.connect()

heroes = Table('heroes', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('name', Text, nullable=False)
)

categories = Table('categories', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('name', Text, nullable=False),
    Column('cover_img', Text, nullable=True)
)

product_types = Table('product_types', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('name', Text, nullable=False)
)

clients = Table('clients', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('phone', Text, nullable=False),
    Column('description', Text, nullable=False)
)

identities = Table('identities', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('name', Text, nullable=False),
    Column('hero_id', ForeignKey('heroes.id')),
    Column('product_type_id', ForeignKey('product_type.id')),
    Column('category_id', ForeignKey('categories.id')),
    Column('description', Text, nullable=False),
    Column('img_path', Text, nullable=False)
)

items = Table('items', data,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('identity_id', ForeignKey('identity.id')),
    Column('size', Text, nullable=False),
    Column('price', Double, nullable=False)
)
