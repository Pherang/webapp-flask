from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# User clas inherits from the SQLAlchemy.Model class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(12), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # An inconcsistency with SQLAlchemy is that
    # in the db.relationship() call the model is referenced by Post, the name of the class representing the table
    # in the db.ForeignKey() call in Post, the table user.id is referenced by its actual table name user,

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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
