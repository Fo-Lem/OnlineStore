from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get('/')
def home():
    return {'message': "Антон - гей"}

@app.get('/category_{category_id}/product_{prod_id}/hero_{hero_id}')
def get_item(category_id:int, prod_id:int, hero_id:int):
    res = jsonable_encoder({'category': category_id, 'product': prod_id, 'hero': hero_id})
    return JSONResponse(content=res)


#filters
@app.get('/category_{category_id}/')
def get_iems_by_category(category_id: int):
    return {'message': "Антон - гей"}

@app.get('/product_{product_id}/')
def get_iems_by_product(product_id):
    return {'message': "Антон - гей"}


@app.get('/hero_{hero_id}/')
def get_iems_by_product(hero_id):
    return {'message': "Антон - гей"}