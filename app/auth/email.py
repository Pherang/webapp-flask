from flask import current_app
from flask_mail import Message
from app import mail
from flask import render_template
from threading import Thread

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
                sender=current_app.config['ADMINS'][0],
                recipients=[user.email],
                text_body=render_template('email/reset_password.txt',
                                          user=user, token=token),
                html_body=render_template('email/reset_password.html',
                                          user=user, token=token))
    print("Email sent")
