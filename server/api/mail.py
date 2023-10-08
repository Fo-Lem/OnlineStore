import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from main import mail_conf

# Define email sender and receiver
EMAIL_SENDER = mail_conf['email_sender']
EMAIL_PASSWORD = mail_conf['email_password']
EMAIL_RECEIVER = mail_conf['email_receiver']

def send_mail(html):
    em = MIMEMultipart()
    em['From'] = EMAIL_SENDER
    em['To'] = EMAIL_RECEIVER
    em['Subject'] = "Новый заказ"
    part2 = MIMEText(html, 'html')
    em.attach(part2)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())