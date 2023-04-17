from tools.extensions import db


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(36), primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    userimage = db.Column(db.String(255))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    salt = db.Column(db.String(255))

    def __init__(self, user_id, firstname, lastname, userimage, username, email, password, salt):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.userimage = userimage
        self.username = username
        self.email = email
        self.password = password
        self.salt = salt

    def __repr__(self):
        return f"<User {self.firstname} {self.lastname}>"
