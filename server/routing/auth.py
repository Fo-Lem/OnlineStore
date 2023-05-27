from fastapi import Body, Header
from fastapi.responses import JSONResponse
from hashlib import md5

from admin.login import create_jwt_token, check_token
from main import conf, app

ADMIN = conf['admin']

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
            token = create_jwt_token(login, password)
            return JSONResponse({'token': token})
        else:
            msg = 'Password is inncorect'
    return JSONResponse({'message': msg})

@app.post('/admin/auth')
def test_token(
        authorization=Header(),
    ):
    token = authorization.split(' ')[1]
    is_valid = check_token(token)
    if is_valid:
        return JSONResponse({'message': 'Token is valid'})
    return JSONResponse({'err': 'Invalid token'})