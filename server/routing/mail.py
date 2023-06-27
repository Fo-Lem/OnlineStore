from fastapi import Body
from fastapi.responses import JSONResponse

from main import app
from api.mail import send_mail

@app.post('/api/mail')
def send_message_to_mail(
    fio=Body(embed=True),
    email=Body(embed=True),
    phone=Body(embed=True),
    receive_method=Body(embed=True),
    total_price=Body(embed=True),
    body=Body(embed=True),
      ):
    try:
        send_mail(fio, email, phone, receive_method, total_price, body)
        return JSONResponse({'msg': 'Message was sending'})
    except:
        return JSONResponse({'err': 'Check your data'})
