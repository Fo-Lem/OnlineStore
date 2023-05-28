from fastapi.responses import JSONResponse

from api.fetch.tabels import fetch_products, fetch_from_table
from main import app

@app.get('/api/data/{table}')
def get_table(table:str):
    if table == 'products':
        return JSONResponse(fetch_products())
    return JSONResponse(fetch_from_table(table))