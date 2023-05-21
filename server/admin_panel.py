from fastapi import File, Body, Form, UploadFile
from hashlib import md5
from sqlalchemy import Row
from typing import Union

import jwt
import time
import shutil
import os

from main import app, JSONResponse, conf
from admin.api import add_entity, update_entity, delete_entity, conn, session
from fetch.json_data import fetch_products, fetch_from_table, heroes, categories,product_types, \
    categories_to_types, identities, items

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: Union[str, None] = None
    cover_img: Union[str, None] = None

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


ADMIN = conf['admin']
SECRET_KEY = conf['secret']
ALGORITHM = conf['algorithm']

@app.post('/admin/login')
def home_admin(
        login:str=Form(),
        password:str=Form()
    ):

    msg:str = 'Login is inccorect'
    admin_login:str = md5(ADMIN['login'].encode()).hexdigest()
    admin_pass:str = md5(ADMIN['password'].encode()).hexdigest()

    if admin_login==login:
        if admin_pass == password:
            payload = {
                'login': login,
                'password': password,
                'expires': time.time()+60*30
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
            return JSONResponse({'token': token})
        else:
            msg = 'Password is inncorect'
    return JSONResponse({'message': msg})

@app.post('/admin/auth')
def home_admin(
        token:str=Form(),
    ):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload['expires'] <= time.time():
            payload=None
    except:
        payload = None
    if payload:
        return JSONResponse({'message': payload})
    return JSONResponse({'message': 'token is not valid'})

@app.post('/admin/image')
def put_image(file:UploadFile=File(), path=Body(embed=True), name=Body(embed=True)):
    cover_path:str = "../imgs/"+path
    try:
        os.mkdir(cover_path)
    except FileExistsError:
        pass
    if cover_path.endswith('/') == False:
        cover_path+='/'
    cover_path=cover_path+name
    with open(cover_path, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return JSONResponse({'image': cover_path})    


@app.post('/admin/category')
def add_category(name=Body(embed=True),cover_img=Body(embed=True)):
    add_entity(categories, name=name, cover_img=cover_img)
    return JSONResponse({
        'name': name,
        'cover_img': cover_img
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
        }, status_code=401)

@app.delete('/admin/category')
def delete_category(id=Body(embed=True)):
    status = 201
    msg = ''
    try:
        session.query(categories_to_types).where(categories_to_types.c.id==id).delete()
        session.commit()
        session.query(categories).where(categories.c.id==id).delete()
        session.commit()
    except Exception as e:
        msg = str(e)
        status = 213

    return JSONResponse({
            'msg': msg,
        }, status_code=status)


@app.post('/admin/hero')
def add_hero(name=Body(embed=True)):
    add_entity(heroes, name=name)
    return JSONResponse({
        'name': name
        },status_code=201)

@app.put('/admin/hero')
def update_hero(id=Body(embed=True), name=Body(embed=True)):
    res = update_entity(heroes, id=id, name=name)
    if res > 0:
        return JSONResponse({
            'name': name,
        },status_code=201)
    else:
        return JSONResponse({
            'err': 'Inncorrect data',
        }, status_code=213)
    

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
    conn.commit()
    identity['id'] = id_
    return JSONResponse(identity, status_code=201)

@app.post('/admin/product_type_to_category')
def set_product_type_to_category(category_id=Body(embed=True),product_type_id=Body(embed=True)):
    res = add_entity(categories_to_types, category_id=category_id, product_type_id=product_type_id)
    conn.commit()
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
    conn.commit()
    return JSONResponse({
            'item_params': item_params,
            'params': params
        }, status_code=201) 
