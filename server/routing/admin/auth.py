from fastapi import Body, Header
from fastapi.responses import JSONResponse
from hashlib import md5

from admin.jwt_token import create_jwt_token, check_token, create_refresh_token, get_payload
from admin.api import delete_entity, conn
from database.structure import refresh_tokens
from main import auth_conf, app

ADMIN = auth_conf['admin']

@app.post('/api/login')
def home_admin(
        login:str=Body(embed=True),
        password:str=Body(embed=True)
    ):

    msg:str = 'Login is inccorect'
    admin_login:str = md5(ADMIN['login'].encode()).hexdigest()
    admin_pass:str = md5(ADMIN['password'].encode()).hexdigest()

    if admin_login==login:
        if admin_pass == password:
            token = create_jwt_token(login)
            refresh_token = create_refresh_token(login)
            return JSONResponse(
                {
                    'token': token,
                    'refresh_token': refresh_token
                }
            )
        else:
            msg = 'Password is inncorect'
    return JSONResponse({'message': msg})

@app.post('/admin/relogin')
def relogin(
        refresh_token:str=Body(embed=True)
    ):
    sel = refresh_tokens.select().where(refresh_tokens.c.id==refresh_token)
    refresh_token_exist = conn.execute(sel)
    
    if refresh_token_exist.first() == None:
        return JSONResponse({'Message': 'Refresh token is not exist'}, status_code=213)
    delete_entity(refresh_tokens, id=refresh_token)

    is_valid = check_token(refresh_token)
    if is_valid:
        login = get_payload(refresh_token)['login']
        token = create_jwt_token(login)
        refresh_token = create_refresh_token(login)
        return JSONResponse(
            {
                'token': token,
                'refresh_token': refresh_token
            }
        )
    else:
        return JSONResponse({'Message': 'Refresh token is not valid'}, status_code=213)

@app.post('/admin/auth')
def test_token(
        authorization=Header(),
    ):
    token = authorization.split(' ')[1]
    is_valid = check_token(token)
    if is_valid:
        return JSONResponse({'message': 'Token is valid'})
    return JSONResponse({'err': 'Invalid token'}, status_code=213)

