from fastapi import File, Body, UploadFile
from fastapi.responses import JSONResponse

import shutil
import os

from main import app, HTTP_RESPONSE_CODE, HTTP_RESPONSE_MESSAGE

@app.post('/admin/image')
def put_image(file:UploadFile=File(), path=Body(embed=True), name=Body(embed=True)):
    cover_path:str = "../imgs/"+path
    try:
        os.mkdir(cover_path)
    except FileExistsError:
        pass
    if cover_path.endswith('/') == False:
        cover_path+='/'
    cover_path=cover_path+name
    with open(cover_path, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return JSONResponse({
        'image': cover_path
    }, status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_CREATED)  


@app.delete('/admin/image')
def delete_image(full_path=Body(embed=True)):
    try:
        os.remove(full_path)
        return JSONResponse({
            'msg': HTTP_RESPONSE_MESSAGE.SUCCESSFUL_DELEATED
        }, status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_DELEATED) 
    except FileExistsError:
        return JSONResponse({"err": "Couldn't to find the file"})
    except:
         return JSONResponse({"err": "Something went wrong"})
    