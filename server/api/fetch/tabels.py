from sqlalchemy import select

from database.structure import categories_to_types, categories, product_types, identities, items,\
      heroes, refresh_tokens, conn

def fetch_products():
    json_res = {}
    sel = select(
        identities, items.c.size, items.c.price, items.c.id
        ).where(items.c.identity_id==identities.c.id)
    for row in conn.execute(sel):
        json_row = {}
        for field in row._fields:
            json_row[field] = row.__getattr__(field)
        json_res[row.id] = json_row
    return json_res


def fetch_from_table(tablename: str):
    tables = {
        'categories': categories,
        'product_types': product_types,
        'heroes': heroes,
        'categories_to_types': categories_to_types,
        'items': items,
        'refresh_tokens': refresh_tokens
    }
    table = tables.get(tablename, None)
    if table == None:
        return {'msg': 'Table not exist!'}
    json_res = {}
    sel = table.select()
    for row in conn.execute(sel):
        json_row = {}
        for field in row._fields:
            json_row[field] = row.__getattr__(field)
        json_res[row.id] = json_row
    return json_res

