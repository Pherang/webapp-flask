from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

# User clas inherits from the SQLAlchemy.Model class and 
# four mixins from UserMixin required for use with Flask-Login
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(12), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # An inconcsistency with SQLAlchemy is that
    # in the db.relationship() call the model is referenced by Post, the name of the class representing the table
    # in the db.ForeignKey() call in Post, the table user.id is referenced by its actual table name user,

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
                digest, size)
    # We've defined our own repr() method below
    # this allows us to control what is returned when repr() is called.
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<post {}>'.format(self.body)

# Flask-Login requires a user_loader function to work because
# it doesn't do anything with databases.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
