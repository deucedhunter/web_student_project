import smtplib, ssl

def send_email(to, message):
    host = 'smtp.gmail.com'
    email_address = 'deucedhunter@gmail.com'
    password = "nnfn mmyz tdmm gsme"
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email_address, password)
        server.sendmail(email_address, to, message)