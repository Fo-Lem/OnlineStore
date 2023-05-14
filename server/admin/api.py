from database.structure import conn

def add_entity(table, **kwargs):
    ins = table.insert().values(**kwargs)
    conn.execute(ins)
