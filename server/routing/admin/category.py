from fastapi import Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union

from main import app, HTTP_RESPONSE_CODE, HTTP_RESPONSE_MESSAGE

from admin.api import add_entity, update_entity, reference_delete, conn
from database.structure import categories, categories_to_types, identities


class Category(BaseModel):
    id: int
    name: Union[str, None] = None
    cover_img: Union[str, None] = None

@app.post('/admin/category')
def add_category(name=Body(embed=True),cover_img=Body(embed=True)):
    category_id = add_entity(categories, name=name, cover_img=cover_img)
    categ_to_type_id = add_entity(categories_to_types, category_id=category_id, product_type_id=-1)
    return JSONResponse({
        'id': category_id,
        'name': name,
        'cover_img': cover_img,
        'categories_to_types_id':categ_to_type_id
        },status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_CREATED)

@app.put('/admin/category')
def update_category(
    category: Category
    ):
    params = {}
    if category.name:
        params['name'] = category.name
    if category.cover_img:
        params['cover_img'] = category.cover_img
    if params == {}:
        return JSONResponse({
            'err': HTTP_RESPONSE_MESSAGE.NO_ANY_PARAMETRS,
        }, status_code=HTTP_RESPONSE_CODE.NO_ANY_PARAMETRS)
    try:
        res = update_entity(categories, id=category.id, **params)
    except:
        res = 0
    if res > 0:
        return JSONResponse({
            'name': category.name,
            'cover_path': category.cover_img
        },status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_MODIFIED)
    else:
        return JSONResponse({
            'err': HTTP_RESPONSE_MESSAGE.INCORRECT_DATA,
        }, status_code=HTTP_RESPONSE_CODE.INCORRECT_DATA)

@app.delete('/admin/category')
def delete_category(id=Body(embed=True)):
    status = HTTP_RESPONSE_CODE.SUCCESSFUL_DELEATED
    msg = HTTP_RESPONSE_MESSAGE.SUCCESSFUL_DELEATED
    try:
        upd = identities.update().where(identities.c.category_id==id).values(category_id=-1)
        conn.execute(upd)
        reference_delete(categories, categories_to_types, id, 'category_id')
    except:
        msg = HTTP_RESPONSE_MESSAGE.ABORTED_DELEATED
        status = HTTP_RESPONSE_CODE.ABORTED_DELEATED

    return JSONResponse({
            'msg': msg,
        }, status_code=status)