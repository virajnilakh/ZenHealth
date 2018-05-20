from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 15

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=397^Egg-Free
&allowedDiet[]=390^Pescetarian&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 15, lunch in course , sugar value is high, allowed allergy: egg, allowedDiet=Pescetarian

no recipes retured for this query
'''                  
                     
