#coding:utf8

from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from datetime import datetime
import os

PATH1 = os.getcwd()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/test.db' % PATH1

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique = True)
    phonenum = db.Column(db.String(20), unique = True)
    company = db.Column(db.String(40))
    position = db.Column(db.String(80))
    stars = db.Columns(db.Integer)
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

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstTrade = db.Column(db.String(30))
    secondTrade = db.Column(db.String(40))

    def __init__(self, firstTrade, secondTrade):
        self.firstTrade = firstTrade
        self.secondTrade = secondTrade
    
    def __repr__(self):
        return "<firstTrade %r>" % self.firstTrade
    
    def to_json(self):
        return {
            'id' : self.id,
            'firstTrade' : self.firstTrade,
            'secondTrade' : self.secondTrade,
        }


class jobType(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    jobTypeName = db.Column(db.String(80))
    tradeName = db.Column(db.String(80))
    
    
    def __init__(self, jobTypeName, tradeName):
        self.jobTypeName = jobTypeName
        self.tradeName = tradeName
       

    def __repr__(self):
        return "<typeName: %r, tradeName: %r, tradeId: %r>" % (self.jobTypeName, self.tradeName, self.tradeId)
    
    def to_json(self):
        return {
            'id' : self.id,
            'jobTypeName' : self.jobTypeName,
            'tradeName' : self.tradeName
        }

class TradeJobTypes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tradeId = db.Column(db.Integer)
    jobTypeId = db.Column(db.Integer)

    def __init__(self, tradeId, jobTypeId):
        self.tradeId = tradeId
        self.jobTypeId = jobTypeId
    
    def __repr__(self):
        return "<tradeId: %r, jobTypeId: %r >" % (self.tradeId, self.jobTypeId)
    
    def to_json(self):
        return {
            'id' : self.id,
            'tradeId' : self.tradeId,
            'jobTypeId' : self.jobTypeId
        }

class userTrades(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer)
    tradeId = db.Column(db.Integer)
    tradeJobTypesId = db.Column(db.Integer)

    def __init__(self, userId, tradeId, tradeJobTypesId):
        self.userId = userId
        self.tradeId = tradeId
        self.tradeJobTypesId = tradeJobTypesId
    
    def __repr__(self):
        return "<userId : %r, tradeId ： %r, tradeJobTypesId : %r >" % (self.userId, self.tradeId, self.tradeJobTypesId)
    
    def to_json(self):
        return {
            'id' : self.id, 
            'userId' : self.userId,
            'tradeId' : self.tradeId,
            'tradeJobTypesId' : self.tradeJobTypesId
        }

class location(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    country = db.Column(db.String(30))
    province = db.Column(db.String(30))
    city = db.Column(db.String(30))

    def __init__(self, id, country, province, city):
        self.id = id
        self.country = country
        self.province = province
        self.city = city
    
    def __repr__(self):
        return "<country : %r, province ： %r, city : %r >" % (self.country, self.province, self.city)
    
    def to_json(self):
        return {
            'id' : self.id, 
            'country' : self.country,
            'province' : self.province,
            'city' : self.city,
        }


class userLocation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer)
    locationId = db.Column(db.Integer)

    def __init__(self, id, userId, locationId):
        self.id = id
        self.userId = userId
        self.locationId = locationId
    
    def __repr__(self):
        return "<userId : %r, locationId ： %r>" % (self.userId, self.locationId)
    
    def to_json(self):
        return {
            'id' : self.id, 
            'userId' : self.userId,
            'locationId' : self.locationId,
        }

class keyWord(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    keyWordName = db.Column(db.String(50))

    def __init__(self, keyWordName):
        self.keyWordName = keyWordName
    
    def __repr__(self):
        return "<keyWordName : %r, keyWordName ： %r>" % (self.keyWordName   
    def to_json(self):
        return {
            'id' : self.id, 
            'keyWordName' : self.keyWordName,
        }


class userKeyWord(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer)
    keyWordId = db.Column(db.Integer)
    kwExperience = db.Column(db.Integer)
    kwquality = db.Column(db.String(20))

   def __init__(self, userId, keyWordId, kwExperience, kwquality):
        self.userId = userId
        self.keyWordId = keyWordId
        self.kwExperience = kwExperience
        self.kwquality = kwquality
    
    def __repr__(self):
        return "<userId: %r, keyWordId : %r, kwExperience ： %r,kwquality: %r >" % (self.userId, self.keyWordId, self.kwquality)
    
    def to_json(self):
        return {
            'id' : self.id, 
            'userId' : self.userId,
            'keyWordId' : self.keyWordId,
            'kwExperience' : self.kwExperience,
            'kwquality' :  self.kwquality,
        }





