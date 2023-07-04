import smtplib
import ssl
from email.message import EmailMessage

from main import mail_conf

# Define email sender and receiver
EMAIL_SENDER = mail_conf['email_sender']
EMAIL_PASSWORD = mail_conf['email_password']
EMAIL_RECEIVER = mail_conf['email_receiver']

def send_mail(receiver, total_price, body, email, phone):
    # Set the subject and body of the email
    subject = 'Новый заказ!!!'
    body = """
    I've just published a new video on YouTube: https://youtu.be/2cZzP9DLlkg
    """

    em = EmailMessage()
    em['From'] = EMAIL_SENDER
    em['To'] = EMAIL_RECEIVER
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, em.as_string())