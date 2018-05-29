from app import db

# 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(12), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # We've defined our own repr() method below
    # this allows us to control what is returned when repr() is called.
    def __repr__(self):
        return '<User {}>'.format(self.username)
