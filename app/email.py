from flask_email import Message
from app import mail

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Mesage(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
