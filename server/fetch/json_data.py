from sqlalchemy import select

from database.structure import categories, product_type, heroes, identity, items, conn

table_set = [categories, product_type, heroes]

def fetch_full_identity():
    pass

def fetch_structure(table_ind, *fields):
    json_res = {}
    table = table_set[table_ind]
    sel = table.select()
    res = conn.execute(sel)

    for row in res:
        json_res[row.id] = {}
        for field in fields:
            json_res[row.id][field] = row.__getattr__(field)
        if table_ind < len(table_set)-1:
            next_table = table_set[table_ind+1]
            json_res[row.id][next_table.fullname] =  fetch_structure(table_ind+1, *next_table.c.keys())


    return json_res

def fetch_with_full_items():
    json_res = fetch_structure(0, 'id', 'name')
    sel_f_it = select(
        identity,
        items.c.size,
        items.c.price
    ).where(items.c.identity_id==identity.c.id)
    full_items = conn.execute(sel_f_it)
    for full_item in full_items:
        item_cat = json_res[full_item.category_id]
        item_prod_type = item_cat['product_type'][full_item.product_type_id]
        cell = item_prod_type['heroes'][full_item.hero_id]
        json_item = {
                    'id': full_item.id,
                    'name': full_item.name,
                    'price': full_item.price,
                    'size': full_item.size,
                    'description': full_item.description
                }
        if 'items' in cell.keys():
            cell['items'].append(json_item)
        else:
            cell.update({'items': [
                json_item
            ]})
    return json_res