from flask import render_template
from app import app

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
