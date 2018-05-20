from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 9

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=397^Egg-Free
&allowedDiet[]=387^Lacto-ovo vegetarian&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 9, desserts in course , sugar value is high, allowed allergy: egg, allowedDiet=Lacto-ovo vegetarian

no recipes retured for this query
'''                  
                     
