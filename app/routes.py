from flask import render_template, flash, redirect, url_for, request

# Imports the app class was assigned Flask from the app folder
from app import app

# Imports the LoginForm class from the app/forms.py module
# app is the package folder
from app.forms import LoginForm

# required to handle logins and sessions for our login view function
from flask_login import current_user, login_user, logout_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kyoto'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Toronto'
        },
        {
            'author': {'username:' 'Susan'},
            'body': 'The Avengers movie was ok'
        }
    ]
    return render_template('index.html', 
            title="Superblog", posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm() #instantiate the LoginForm class
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # login_user is a Flask-Login function that will
        # set current_user to the user. Saves the session..
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
