from fetch.__req_db_struct import *

table_set = [categories, product_types, heroes]

def fetch_short_structure(table_ind:int, *fields):
    json_res = {}
    table = table_set[table_ind]
    sel = table.select()
    res = conn.execute(sel)

    for row in res:
        json_res[row.id] = {}
        for field in fields:
            json_text = None 
            try:
                json_text = row.__getattr__(field)
            except AttributeError:
                pass
            json_res[row.id][field] = json_text
        if table_ind < len(table_set)-1:
            next_table = table_set[table_ind+1]
            json_res[row.id][next_table.fullname] =  fetch_short_structure(table_ind+1, *next_table.c.keys())
    return json_res