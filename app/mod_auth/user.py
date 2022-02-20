from sqlalchemy.ext.hybrid import hybrid_property
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    pass_hash = db.Column(db.String(128))

    def __init__(self, username, email, pass_hash):
        self.username = username
        self.email = email
        self.pass_hash = pass_hash

    def __repr__(self):
        return f"<User {self.username}>"
