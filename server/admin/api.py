from sqlalchemy import Row
from sqlalchemy import delete, Table
from sqlalchemy.orm import Session

from database.structure import conn

session = Session(conn.engine)

def add_entity(table, **kwargs):
    ins = table.insert().values(**kwargs)
    res = conn.execute(ins)
    return res.inserted_primary_key.id

def update_entity(table, id, **kwargs):
    upd = table.update().where(table.c.id==id).values(**kwargs)
    res:Row = conn.execute(upd)
    return res.rowcount


def delete_entity(table:Table, id:int):
    session.query(table).where(table.c.id==id).delete()