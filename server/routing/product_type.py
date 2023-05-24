from fastapi import Body

from main import app, JSONResponse
from admin.api import add_entity, update_entity, reference_delete
from fetch.json_data import product_types, categories_to_types

@app.post('/admin/product_type')
def add_product_type(category_id:str=Body(embed=True),name=Body(embed=True)):
    try:
        product_type_id = add_entity(product_types, name=name)
        res = add_entity(categories_to_types, category_id=category_id, product_type_id=product_type_id)
        return JSONResponse({
            'name': name,
            'product_type_id': product_type_id,
            'c_t_p': res
            },status_code=201)
    except:
        return JSONResponse({
            'err': 'Incorrect data'
            },status_code=213)

@app.put('/admin/product_type')
def update_product_type(id=Body(embed=True), name=Body(embed=True)):
    res = update_entity(product_types, id=id, name=name)
    if res > 0:
        return JSONResponse({
            'name': name,
        },status_code=201)
    else:
        return JSONResponse({
            'err': 'Inncorrect data',
        }, status_code=213)
    

@app.delete('/admin/product_type')
def delete_product_type(id=Body(embed=True)):
    try:
        reference_delete(product_types, categories_to_types, id, 'product_type_id')
    except Exception as e:
        msg = str(e)
        status = 213

    return JSONResponse({
            'msg': msg,
        }, status_code=status)
