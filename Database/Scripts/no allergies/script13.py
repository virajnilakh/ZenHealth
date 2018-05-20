from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 13

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey
&allowedDiet[]=389^ Ovo vegetarian&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 13, desserts in course , sugar value is high, allowed allergy: none, allowedDiet=Ovo vegetarian;

no result for this query
'''                  
                     
