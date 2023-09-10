from fastapi import FastAPI, Response, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from config import Config
#from routing.admin.auth import check_token

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
    response = await call_next(request)
    if target_is_admin.startswith('/admin'):
        auth = request.headers.get('Authorization')
        if auth:
            token = auth.split(' ')[1]
            is_valid = check_token(token)
            if is_valid:
                return RedirectResponse('/api/catalog')
        return RedirectResponse('/index.html')
    return response

@app.get('/admin')
def test():
    return ''

import routing.clients.catalog 
import routing.clients.tables 

#include admin panel
import admin.panel
import routing.mail