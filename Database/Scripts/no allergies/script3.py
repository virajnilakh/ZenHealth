from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 3

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey
&allowedDiet[]=389^Ovo vegetarian&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 3, Main Dishes in course , sugar value is high, allowed allergy: none, allowedDiet=Ovo vegetarian;

no result for this query
'''                  
                     
