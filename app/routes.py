from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse

# Imports the app class was assigned Flask from the app folder
from app import app, db

# Imports the LoginForm class from the app/forms.py module
# app is the package folder
from app.forms import LoginForm, RegistrationForm, EditProfileForm

# required to handle logins and sessions for our login view function
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

from datetime import datetime

@app.before_request
def before_request():
    # a reference to current_user will open a session to the database.
    # which is why db.session.add() isn't here.
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/')
@app.route('/index')
@login_required # this is initialized in app/__init__.py
def index():
    user = {'username': 'Kyoto'}
    posts = [
        { 'author': {'username': 'John'}, 'body': 'Beautiful day in Toronto'
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
        
        # The @login_required decorator will redirect here and 
        # add a query string ?next=/index which can be processed to redirect
        # the user to where they wanted to go. However it can be abused
        # so it must be parsed.
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                            form=form)
