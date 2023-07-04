from fastapi.responses import JSONResponse

from api.fetch.structure import fetch_full_structure
from main import app

@app.get('/api/catalog/')
def get_catalog():
    return JSONResponse(fetch_full_structure())
