from flask import render_template, flash, redirect

# Imports the app class was assigned Flask from the app folder
from app import app

# Imports the LoginForm class from the app/forms.py module
# app is the package folder
from app.forms import LoginForm

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
            title="Superblog", posts=posts, user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm() #instantiate the LoginForm class
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
