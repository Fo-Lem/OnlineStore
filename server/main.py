from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config import Config

from fetch.json_data import fetch_full_structure

app = FastAPI()
conf = Config('conf/auth.conf')

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

@app.get('/api/catalog/')
def home():
    return fetch_full_structure()

#include admin panel
from admin_panel import *