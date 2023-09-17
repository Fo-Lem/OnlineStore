from fastapi import Body, Header
from fastapi.responses import JSONResponse
from hashlib import md5

from admin.jwt_token import create_jwt_token, check_token, create_refresh_token, get_payload
from admin.api import delete_entity, conn
from database.structure import refresh_tokens
from main import auth_conf, app, HTTP_RESPONSE_CODE, HTTP_RESPONSE_MESSAGE

ADMIN = auth_conf['admin']

@app.post('/api/login')
def home_admin(
        login:str=Body(embed=True),
        password:str=Body(embed=True)
    ):

    msg:str = HTTP_RESPONSE_MESSAGE.INCORRECT_LOGIN
    _status_code = HTTP_RESPONSE_CODE.INCORRECT_LOGIN
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
                }, status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_CREATED
            )
        else:
            msg = HTTP_RESPONSE_MESSAGE.INCORRECT_PASSWORD
    return JSONResponse({'err': msg}, status_code=_status_code)

@app.post('/api/relogin')
def relogin(
        refresh_token:str=Body(embed=True)
    ):
    sel = refresh_tokens.select().where(refresh_tokens.c.id==refresh_token)
    refresh_token_exist = conn.execute(sel)
    
    if refresh_token_exist.first() == None:
        return JSONResponse({
            'err':  HTTP_RESPONSE_MESSAGE.REFRESH_TOKEN_NOT_EXIST
        }, status_code=HTTP_RESPONSE_CODE.REFRESH_TOKEN_NOT_EXIST)
    
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
            }, status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_CREATED
        )
    else:
        return JSONResponse({
            'err': HTTP_RESPONSE_MESSAGE.REFRESH_TOKEN_NOT_VALID
        }, status_code=HTTP_RESPONSE_CODE.REFRESH_TOKEN_NOT_VALID)

@app.post('/admin/auth')
def test_token(
        authorization=Header(),
    ):
    token = authorization.split(' ')[1]
    is_valid = check_token(token)
    if is_valid:
        return JSONResponse({'msg': HTTP_RESPONSE_MESSAGE.JWT_TOKEN_IS_VALID})
    return JSONResponse({
        'err': HTTP_RESPONSE_MESSAGE.JWT_TOKEN_NOT_VALID
    }, status_code=HTTP_RESPONSE_CODE.JWT_TOKEN_NOT_VALID)

