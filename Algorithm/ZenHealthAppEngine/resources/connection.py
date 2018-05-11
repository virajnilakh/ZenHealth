from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from flask import Flask
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://u:p@h/d"
    #os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)


class UserProfile(db.Model):

    __tablename__ = 'userProfile'

    uname = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    medication = db.Column(db.String(100))
    diabetes_type = db.Column(db.String(15))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    gender = db.Column(db.String(10))
    diet = db.Column(db.String(20))
    diabetes_type = db.Column(db.String(15))
    allergies = db.Column(db.String(50))
    age = db.Column(db.Integer)


    def __init__(self,uname):
       self.uname = uname

class UserCredential (db.Model):
    __tablename__ = 'userCredential'

    uname = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))
    foodConsumed = db.relationship('FoodConsumed', backref='userCredential', lazy=True)


class FoodConsumed(db.Model):
    __tablename__ = 'foodConsumed'


    course = db.Column(db.String(50))
    consumed_date = db.Column('date', db.DateTime)
    fooditem  = db.Column(db.String(100))
    timestamp  = db.Column(db.DateTime, primary_key=True)
    uname  = db.Column(db.String(100) , db.ForeignKey('userCredential.uname'),nullable =False)
    suggested  = db.Column(db.Boolean)


    def __init__(self,uname):
       self.uname = uname