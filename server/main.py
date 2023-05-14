from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from fetch.json_data import fetch_full_structure

app = FastAPI()

@app.get('/api/catalog/')
def home():
    return fetch_full_structure()

@app.get('/api/category_{category_id}/product_{prod_id}/hero_{hero_id}')
def get_item(category_id:int, prod_id:int, hero_id:int):
    res = jsonable_encoder({'category': category_id, 'product': prod_id, 'hero': hero_id})
    return JSONResponse(content=res)


#filters
@app.get('/api/category_{category_id}/')
def get_iems_by_category(category_id: int):
    return {'message': "Антон - гей"}

@app.get('/api/product_{product_id}/')
def get_iems_by_product(product_id):
    return {'message': "Антон - гей"}


@app.get('/api/hero_{hero_id}/')
def get_iems_by_product(hero_id):
    return {'message': "Антон - гей"}


#include admin panel
from admin_panel import *