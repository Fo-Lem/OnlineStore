from fastapi import Body
from fastapi.responses import JSONResponse

from main import app, HTTP_RESPONSE_CODE, HTTP_RESPONSE_MESSAGE
from admin.api import add_entity, update_entity, delete_entity
from database.structure import heroes

@app.post('/admin/hero')
def add_hero(name=Body(embed=True)):
    hero_id = add_entity(heroes, name=name)
    return JSONResponse({
        'id': hero_id,
        'name': name
        },status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_CREATED)

@app.put('/admin/hero')
def update_hero(id=Body(embed=True), name=Body(embed=True)):
    res = update_entity(heroes, id=id, name=name)
    if res > 0:
        return JSONResponse({
            'name': name,
        },status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_MODIFIED)
    else:
        return JSONResponse({
            'err': HTTP_RESPONSE_CODE.INCORRECT_DATA,
        }, status_code=HTTP_RESPONSE_MESSAGE.INCORRECT_DATA)
    
@app.delete('/admin/hero')
def delete_hero(id=Body(embed=True)):
    delete_entity(heroes, id=id)
    return JSONResponse({
        'msg': HTTP_RESPONSE_MESSAGE.SUCCESSFUL_DELEATED
        },status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_DELEATED)