import smtplib, ssl
import os


def sendmail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "fornewsapp@gmail.com"
    password =os.getenv("PASSWORD")

    receiver ="fornewsapp@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
