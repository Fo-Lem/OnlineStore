from fastapi import Body
from fastapi.responses import JSONResponse

from main import app

@app.post('/api/mail')
def send_message_to_mail(name=Body(embed=True)):
    return JSONResponse({'msg': 'Message was sending'})
