import smtplib, ssl
import os
def send_email(to, message):
    host = 'smtp.gmail.com'
    email_address = 'deucedhunter@gmail.com'
    password = os.getenv('PASSWORD')
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email_address, password)
        server.sendmail(email_address, to, message)