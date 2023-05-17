from fastapi import File, Body

from main import app, JSONResponse
from admin.api import add_entity
from fetch.json_data import fetch_products, fetch_from_table

@app.get('/admin')
def home_admin():
    return JSONResponse({'message': 'You are in admin panel'})

@app.get('/admin/data/{table}')
def show_products(table:str):
    if table == 'products':
        return JSONResponse(fetch_products())
    return JSONResponse(fetch_from_table(table))

@app.post('/admin/category')
def add_category(name=Body(embed=True),file=File()):
    # add_entity(categories, name=name, cover_img=cover_img)
    return JSONResponse({
        'name': name,
        'filename': str(next(file.read()))
        })

