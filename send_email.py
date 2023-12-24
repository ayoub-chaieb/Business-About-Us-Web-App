import smtplib, ssl
import os


def send_email(email_address, topic, message: str):
    host = "smtp.gmail.com"
    port = 465
    password = os.getenv("STREAMLIT_WEB_APP_GMAIL_PASSWORD")
    receiver = "ayoubchaieb75@gmail.com"
    email = f"""\
Subject: {email_address} wanted to contact you! || Streamlit Business Contact Us App

From: {email_address}
About: {topic}
{message}
"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email_address, password)
        server.sendmail(email_address, receiver, email)
