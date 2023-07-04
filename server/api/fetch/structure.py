from sqlalchemy import select

from api.fetch.tabels import fetch_from_table, fetch_products
from database.structure import categories_to_types, categories, product_types, heroes, conn

table_set = [categories, product_types, heroes]

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
    
    json_heroes = fetch_from_table('heroes')
    json_items = fetch_products()

    json_res = {
        'categories': json_categories,
        'heroes': json_heroes,
        'items': json_items,
    }
    return json_res




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