from fastapi import Body

from main import app, JSONResponse
from admin.api import add_entity
from database.structure import categories

@app.get('/admin')
def home_admin():
    return JSONResponse({'message': 'You are in admin panel'})

@app.post('/admin/category')
def add_category(name: str=Body(...,embed=True), cover_img: str=Body(...,embed=True)):
    # add_entity(categories, name=name, cover_img=cover_img)
    return JSONResponse({'message': 'Successful'})