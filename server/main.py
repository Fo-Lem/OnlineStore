from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import Config

app = FastAPI()
auth_conf = Config('conf/auth.conf')
mail_conf = Config('conf/mail.conf')

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

import routing.clients.catalog 
import routing.clients.tables 

#include admin panel
import admin.panel
import routing.mail