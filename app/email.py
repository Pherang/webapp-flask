from app import app
from flask_mail import Message
from app import mail
from flask import render_template
from threading import Thread

def async_send_email(app, msg):
    with app.app_context(): # Here we are creating the application context from the Flask app we passed from Thread below
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # The app argument below is the Flask instance
    Thread(target=async_send_email, args=(app, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
                sender=app.config['ADMINS'][0],
                recipients=[user.email],
                text_body=render_template('email/reset_password.txt',
                                          user=user, token=token),
                html_body=render_template('email/reset_password.html',
                                          user=user, token=token))
    print("Email sent")
