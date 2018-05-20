from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 22

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey
&allowedDiet[]=388^Lacto vegetarian&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 22, lunch and snacks in course , sugar value is high, allowed allergy: none, allowedDiet=Lacto vegetarian; 

no result for this query
'''                  
                     
