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