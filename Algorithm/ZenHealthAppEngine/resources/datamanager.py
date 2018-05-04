
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
#import firebase_admin


# # Get a database reference to our posts

#root = db.reference()


#dinos = db.reference('https://zenhealth-215f6.firebaseio.com/foodData')
# fd = db.reference('foodData')

# Retrieve the five tallest dinosaurs in the database sorted by height.
# 'result' will be a sorted data structure (list or OrderedDict).
#result = dinos.order_by_child('sugarLevel').limit_to_last(5).get()
#food_db_ref = firebase.database().ref('foodData');
# # Get a database reference to our posts
# user_db_ref = db.reference('https://zenhealth-215f6.firebaseio.com/foodData.json')

food_db = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)
user_db = firebase.FirebaseApplication('https://zenhealth-215f6-25c67.firebaseio.com/', authentication=None)
