from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config import Config

from fetch.json_data import fetch_full_structure, fetch_from_table, fetch_products

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

@app.get('/api/data/{table}')
def show_products(table:str):
    if table == 'products':
        return JSONResponse(fetch_products())
    return JSONResponse(fetch_from_table(table))

#include admin panel
from admin.panel import *
# from mail import *