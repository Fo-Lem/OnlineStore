from sqlalchemy import select

from fetch.__req_db_struct import *
from ._partial_struct import fetch_short_structure

def fetch_full_structure():
    json_res = fetch_short_structure(0, 'id', 'name', 'cover_path')
    sel_f_it = select(
        identities,
        items.c.size,
        items.c.price
    ).where(items.c.identity_id==identities.c.id)
    full_items = conn.execute(sel_f_it)
    for full_item in full_items:
        item_cat = json_res[full_item.category_id]
        item_prod_type = item_cat['product_types'][full_item.product_type_id]
        cell = item_prod_type['heroes'][full_item.hero_id]
        json_item = {
                    'id': full_item.id,
                    'name': full_item.name,
                    'price': full_item.price,
                    'size': full_item.size,
                    'description': full_item.description,
                    'img_path': full_item.img_path
                }
        if 'items' in cell.keys():
            cell['items'].append(json_item)
        else:
            cell.update({'items': [
                json_item
            ]})
    return json_res