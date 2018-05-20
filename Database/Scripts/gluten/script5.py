from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 5

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedDiet[]=387^Lacto-ovo%20vegetarian&allowedCourse[]=course^course-Main%20Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 5, main dishes in course , sugar value is low, allowed allergy: gluten, allowedDiet= Lacto-ovo vegetarian

no results
'''                  
                     
