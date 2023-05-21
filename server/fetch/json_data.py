from sqlalchemy import select

from fetch.__req_db_struct import *
from ._partial_struct import fetch_short_structure

def fetch_full_structure():
    
    json_categories = {}
    sel = select(
        categories_to_types, 
        categories, 
        product_types
           ).where(
        categories_to_types.c.category_id==categories.c.id, 
        categories_to_types.c.product_type_id==product_types.c.id
        )
    result = conn.execute(sel)
    for row in result:
        row_tuple = row.tuple()
        category_id = row.category_id
        product_type = {
            'id': row.product_type_id,
            'name': row_tuple[7]
        }
        if json_categories.get(category_id, False) == False:
            category = {
                'id': row.category_id,
                'name': row.name,
                'cover_path': row_tuple[5]
            }
            json_categories[category_id] = category
        try: 
            json_categories[category_id]['product_types'][row.product_type_id] = product_type
        except KeyError:
            json_categories[category_id]['product_types'] = {
                row.product_type_id: product_type
            }
    
    heroes = fetch_from_table('heroes')
    json_items = fetch_products()

    json_res = {
        'categories': json_categories,
        'heroes': heroes,
        'items': json_items,
    }
    return json_res


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
