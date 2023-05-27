from fastapi import Body
from fastapi.responses import JSONResponse

from main import app
from admin.api import add_entity, update_entity, delete_entity
from fetch.json_data import heroes

@app.post('/admin/hero')
def add_hero(name=Body(embed=True)):
    hero_id = add_entity(heroes, name=name)
    return JSONResponse({
        'id': hero_id,
        'name': name
        },status_code=201)

@app.put('/admin/hero')
def update_hero(id=Body(embed=True), name=Body(embed=True)):
    res = update_entity(heroes, id=id, name=name)
    if res > 0:
        return JSONResponse({
            'name': name,
        },status_code=201)
    else:
        return JSONResponse({
            'err': 'Inncorrect data',
        }, status_code=213)
    
@app.delete('/admin/hero')
def delete_hero(id=Body(embed=True)):
    delete_entity(heroes, id=id)
    return JSONResponse({
        'msg': 'Deleted'
        },status_code=201)