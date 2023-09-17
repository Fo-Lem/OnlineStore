from fastapi import Body
from fastapi.responses import JSONResponse

from main import app, HTTP_RESPONSE_MESSAGE, HTTP_RESPONSE_CODE
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
        return JSONResponse({'msg': HTTP_RESPONSE_MESSAGE.SUCCESSFUL_SENT})
    except:
        return JSONResponse({
            'err': HTTP_RESPONSE_MESSAGE.INCORRECT_DATA
          }, status_code=HTTP_RESPONSE_CODE.INCORRECT_DATA)
