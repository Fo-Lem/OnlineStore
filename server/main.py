from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'message': "Антон - гей"}

@app.get('/category/')
def get_iems_by_category():
    return {'message': "Антон - гей"}    

@app.get('/items/')
def get_iems_by_type():
    return {'message': "Антон - гей"}