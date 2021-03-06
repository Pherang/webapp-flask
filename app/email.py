from flask_mail import Message
from app import mail
from flask import render_template
from threading import Thread
from flask import current_app

def async_send_email(app, msg):
    with app.app_context(): # Here we are creating the application context from the Flask app we passed from Thread below
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body,
                attachments=None, sync=False):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)
    if sync:
        mail.send(msg)
    else:
        Thread(target=async_send_email,
                args=(current_app._get_current_object(), msg)).start()
