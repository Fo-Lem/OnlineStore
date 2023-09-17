from fastapi import Body
from fastapi.responses import JSONResponse

from main import app, HTTP_RESPONSE_CODE, HTTP_RESPONSE_MESSAGE
from admin.api import add_entity, update_entity, reference_delete
from database.structure import categories_to_types, product_types

@app.post('/admin/product_type')
def add_product_type(category_id:str=Body(embed=True),name=Body(embed=True)):
    try:
        product_type_id = add_entity(product_types, name=name)
        res = add_entity(categories_to_types, category_id=category_id, product_type_id=product_type_id)
        return JSONResponse({
            'name': name,
            'product_type_id': product_type_id,
            'c_t_p': res
            },status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_CREATED)
    except:
        return JSONResponse({
            'err': HTTP_RESPONSE_MESSAGE.INCORRECT_DATA
        },status_code=HTTP_RESPONSE_CODE.INCORRECT_DATA)

@app.put('/admin/product_type')
def update_product_type(id=Body(embed=True), name=Body(embed=True)):
    res = update_entity(product_types, id=id, name=name)
    if res > 0:
        return JSONResponse({
            'name': name,
        },status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_MODIFIED)
    else:
        return JSONResponse({
            'err': HTTP_RESPONSE_MESSAGE.INCORRECT_DATA,
        }, status_code=HTTP_RESPONSE_CODE.INCORRECT_DATA)
    

@app.delete('/admin/product_type')
def delete_product_type(id=Body(embed=True)):
    msg = HTTP_RESPONSE_MESSAGE.SUCCESSFUL_DELEATED
    status=HTTP_RESPONSE_CODE.SUCCESSFUL_DELEATED
    try:
        reference_delete(product_types, categories_to_types, id, 'product_type_id')
    except:
        msg = HTTP_RESPONSE_MESSAGE.ABORTED_DELEATED
        status = HTTP_RESPONSE_CODE.ABORTED_DELEATED

    return JSONResponse({
            'msg': msg,
        }, status_code=status)
