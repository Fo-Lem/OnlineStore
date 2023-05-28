from sqlalchemy import Row
from sqlalchemy import delete, Table

from database.structure import conn

def add_entity(table, **kwargs):
    ins = table.insert().values(**kwargs)
    res = conn.execute(ins)
    conn.commit()
    return res.inserted_primary_key.id

def update_entity(table, id, **kwargs):
    upd = table.update().where(table.c.id==id).values(**kwargs)
    res:Row = conn.execute(upd)
    conn.commit()
    return res.rowcount


def delete_entity(table:Table, id:int):
    del_ = delete(table).where(table.c.id==id)
    conn.execute(del_)
    conn.commit()

def reference_delete(main_table, reference_table, id_:int, refernce_field:str, main_field:str='id'):
    delctt_ = delete(reference_table).where(reference_table.c.__getattr__(refernce_field)==id_)
    delc_ = delete(main_table).where(main_table.c.__getattr__(main_field)==id_)
    conn.execute(delctt_)
    conn.execute(delc_)
    conn.commit()