from fastapi import Body, Header
from fastapi.responses import JSONResponse
from hashlib import md5

import jwt
import time

from main import conf, app

ADMIN = conf['admin']
SECRET_KEY = conf['secret']
ALGORITHM = conf['algorithm']

@app.post('/admin/login')
def home_admin(
        login:str=Body(embed=True),
        password:str=Body(embed=True)
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
        authorization = Header(),
    ):
    token = authorization.split(' ')[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload['expires'] <= time.time():
            payload=None
    except Exception as e:
        payload = str(e)
    if payload:
        return JSONResponse({'message': payload})
    return JSONResponse({'message': 'token is not valid'})