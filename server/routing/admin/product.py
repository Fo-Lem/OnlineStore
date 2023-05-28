from fastapi import Body
from fastapi.responses import JSONResponse
from typing import Union

from main import app
from admin.api import add_entity, update_entity, reference_delete
from database.structure import categories_to_types, identities, items

from pydantic import BaseModel

class Product(BaseModel):
    id: Union[int, None] = None
    name: Union[str, None] = None
    hero_id:Union[int, None] = None
    product_type_id:Union[int, None] = None
    category_id:Union[int, None]=None
    description:Union[str, None]=None
    img_path:Union[str, None]=None
    size:Union[str, None]=None
    price:Union[float, None]=None
    art:Union[str, None]=None
    id_1:Union[int, None]=None  

@app.post('/admin/product')
def add_product(
    product:Product
    ):
    identity = {
        'name': product.name,
        'category_id': product.category_id,
        'product_type_id': product.product_type_id,
        'hero_id': product.hero_id,
        'description': product.description,
        'art': product.art,
        'img_path': product.img_path
    }
    identity_id:int = add_entity(identities, **identity)
    item = {
        'identity_id': identity_id,
        'size': product.size,
        'price': product.price
    }
    id_ = add_entity(items, **item)
    identity.update(item)
    identity['id'] = id_
    return JSONResponse(identity, status_code=201)

@app.post('/admin/product_type_to_category')
def set_product_type_to_category(category_id=Body(embed=True),product_type_id=Body(embed=True)):
    res = add_entity(categories_to_types, category_id=category_id, product_type_id=product_type_id)
    return JSONResponse({'id': res}, status_code=201)

@app.put('/admin/product')
def update_product(
    product:Product
    ):
    params = product.dict(exclude_none=True)
    if params.get('id', None) == None:
        return JSONResponse({
            'err': 'Id value is nessasary',
        }, status_code=213) 
    #update_entity(items, params['id_1'])
    item = ['size', 'price']
    item_params = {}
    for param in item:
        if params.get(param):
            item_params[param]=params.pop(param)
    if item_params!={} and params.get('id_1', None)==None:
        return JSONResponse({
            'msg': 'item parameter is nessasary',
        }, status_code=213)
    elif item_params!={}:
        item_id = params.pop('id_1')
        update_entity(items, item_id, **item_params)
    identity_id = params.pop('id')
    update_entity(identities, identity_id, **params)
    return JSONResponse({
            'item_params': item_params,
            'params': params
        }, status_code=201) 


@app.delete('/admin/product')
def delete_product(id=Body(embed=True)):
    status = 201
    msg = 'Deleted'
    try:
        reference_delete(identities, items, id, 'identity_id')
    except Exception as e:
        msg = str(e)
        status = 213

    return JSONResponse({
            'msg': msg,
        }, status_code=status)