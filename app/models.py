from app import db

# User clas inherits from the SQLAlchemy.Model class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(12), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # An inconcsistency with SQLAlchemy is that
    # below the model is referenced by Post, the name of the class representing the table
    # in the db.ForeignKey() call, for user.id the table is referenced by its actual table name user,
    posts = db.relationship('Post', backref='author', lazy='dynamic')

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
