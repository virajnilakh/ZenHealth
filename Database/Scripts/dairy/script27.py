from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 27

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=mutton&allowedCourse[]=course^course-Salads&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 27, salads in course, sugar value is High, allowed allergy: dairy, mutton in allowed ingredient

there are 0 recipes for this combination 
'''                  
                     
