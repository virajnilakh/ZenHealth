from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 25

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey
&allowedDiet[]=387^Lacto-ovo vegetarian&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 25, lunch and snacks in course , sugar value is high, allowed allergy: none, allowedDiet=Lacto-ovo vegetarian; 

no result for this query/recipes returned already exist in db
'''                  
                     
