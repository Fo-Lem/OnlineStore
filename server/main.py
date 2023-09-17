from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from config import Config
from http_resp.codes import HTTP_RESPONSE_CODE
from http_resp.message import HTTP_RESPONSE_MESSAGE

app = FastAPI()
auth_conf = Config('conf/auth.conf')
mail_conf = Config('conf/mail.conf')

from admin.jwt_token import check_token

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware('/http')
async def authorization_controller(request: Request, call_next):
    target_is_admin: str = request.url.path
    if target_is_admin.startswith('/admin'):
        auth = request.headers.get('Authorization', 'n o')
        token = auth.split(' ')[1]
        is_valid = check_token(token)
        if not is_valid:
            return JSONResponse({
                'err': HTTP_RESPONSE_MESSAGE.ACCESS_DENIED
            }, status_code=HTTP_RESPONSE_CODE.ACCESS_DENIED)
    response = await call_next(request)
    return response

@app.get('/admin')
def test():
    return 'You have access to admin panel!'

import routing.clients.catalog 
import routing.clients.tables 

#include admin panel
import admin.panel
import routing.mail