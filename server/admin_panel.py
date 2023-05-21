from fastapi import File, Body, Form
from hashlib import md5

import jwt
import time

from main import app, JSONResponse, conf
from admin.api import add_entity
from fetch.json_data import fetch_products, fetch_from_table

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

@app.post('/admin/category')
def add_category(name=Body(embed=True),file=File()):
    # add_entity(categories, name=name, cover_img=cover_img)
    return JSONResponse({
        'name': name,
        'filename': str(next(file.read()))
        })

