from flask import render_template
from app import app, db # Remember app is the flask app.

@app.errorhandler(404)
def note_found_error(error):
    return render_template('404.html'), 404 
    # Flask converts return values in view function into response objects 
    # so the above can be in the format (response, status, headers) even

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
