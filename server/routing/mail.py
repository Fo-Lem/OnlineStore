from fastapi import Body, Response
from fastapi.responses import JSONResponse
from datetime import datetime

from main import app, HTTP_RESPONSE_MESSAGE, HTTP_RESPONSE_CODE
from api.mail import send_mail

html = ''
row_template = ''
with open('templates/mail/index.html', 'r') as f:
    html = f.read()
with open('templates/mail/row.html', 'r') as f:
    row_template = f.read()

def paste_value_to_html_template(s:str, **kwargs):
    for arg in kwargs:
        s=s.replace('{'+arg+'}', str(kwargs[arg]))
    return s

@app.post('/api/mail')
def send_message_to_mail(
    fio=Body(embed=True),
    email=Body(embed=True),
    phone=Body(embed=True),
    order=Body(embed=True),
    delivery_address=Body(embed=True),
    total_price=Body(embed=True)
      ):
    global html, row_template
    table = ''
    try:
        for key in order:
            p = paste_value_to_html_template(
                row_template, name=order[key]['name'],
                article=order[key]['article'],
                count=order[key]['count'],
                price=order[key]['price'],
                img_path=order[key]['img_path']
            )
            table += p
        html=paste_value_to_html_template(
            html, table=table,
            fio=fio, 
            mail=email, 
            number=phone, 
            total_price=total_price,
            delivery_address=delivery_address,
            date=datetime.now().date().strftime('%d.%m.%Y')
          )
        send_mail(html=html)
        return JSONResponse({
            'msg': HTTP_RESPONSE_MESSAGE.SUCCESSFUL_SENT}, 
            status_code=HTTP_RESPONSE_CODE.SUCCESSFUL_SENT
        )
    except:
        return JSONResponse({
            'err': HTTP_RESPONSE_MESSAGE.INCORRECT_DATA
          }, status_code=HTTP_RESPONSE_CODE.INCORRECT_DATA)
