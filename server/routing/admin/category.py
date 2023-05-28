from fastapi import Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union

from main import app

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
        },status_code=201)

@app.put('/admin/category')
def update_category(
    category: Category
    ):
    params = {}
    if category.name:
        params['name'] = category.name
    if category.cover_img:
        params['cover_img'] = category.cover_img
    try:
        res = update_entity(categories, id=category.id, **params)
    except:
        res = 0
    if res > 0:
        return JSONResponse({
            'name': category.name,
            'cover_path': category.cover_img
        },status_code=201)
    else:
        return JSONResponse({
            'err': 'Inncorrect data',
        }, status_code=213)

@app.delete('/admin/category')
def delete_category(id=Body(embed=True)):
    status = 201
    msg = 'Deleted'
    try:
        upd = identities.update().where(identities.c.category_id==id).values(category_id=-1)
        conn.execute(upd)
        reference_delete(categories, categories_to_types, id, 'category_id')
    except Exception as e:
        msg = str(e)
        status = 213

    return JSONResponse({
            'msg': msg,
        }, status_code=status)