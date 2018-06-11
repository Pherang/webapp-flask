from flask import render_template
from flask import current_app # Remember app is the flask app.
from app import db 
from app.errors import bp

@bp.app_errorhandler(404)
def note_found_error(error):
    return render_template('errors/404.html'), 404 
    # Flask converts return values in view function into response objects 
    # so the above can be in the format (response, status, headers) even

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
