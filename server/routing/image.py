from fastapi import File, Body, UploadFile

import shutil
import os

from main import app, JSONResponse

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
    return JSONResponse({'image': cover_path})  


@app.delete('/admin/image')
def delete_image(full_path=Body(embed=True)):
    try:
        os.remove(full_path)
        return JSONResponse({'msg': 'Delete successful'}) 
    except FileExistsError:
        return JSONResponse({"msg": "Couldn't to find the file"})
    except:
         return JSONResponse({"msg": "Something went wrong"})
    