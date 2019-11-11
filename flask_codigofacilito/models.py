from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(255))
    comments = db.relationship('Comment')
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, password, email):
        self.username = username
        self.password = self.__create_password(password)
        self.email = email
    
    def __create_password(self, password):
        return generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
