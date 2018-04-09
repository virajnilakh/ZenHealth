
'''
from pymongo import MongoClient
client = MongoClient('hostname', 27017)
db = client.database_name
collection = db.collection_name
collection.find_one({"name":"name1"})
'''
from firebase import firebase
# Import database module.
from firebase_admin import db

# Get a database reference to our posts
food_db_ref = db.reference('https://zenhealth-215f6.firebaseio.com/')
# Get a database reference to our posts
user_db_ref = db.reference('https://zenhealth-215f6-25c67.firebaseio.com/')

food_db = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)
user_db = firebase.FirebaseApplication('https://zenhealth-215f6-25c67.firebaseio.com/', authentication=None)
