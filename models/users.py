#coding:utf8

from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/guoxian1/linni/test.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique = True)
    phonenum = db.Column(db.String(20), unique = True)
    create_date = db.Column(db.DateTime)

    def __init__(self, username, email, phonenum, create_date = None):
        self.username = username
        self.email = email
        self.phonenum = phonenum
        if create_date is None:
            create_date = datetime.utcnow()

    def __repr__(self):
        return "<User %r>" % self.username

    def to_json(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'phonenum' : self.phonenum,
            'create_date' : self.create_date
        }
