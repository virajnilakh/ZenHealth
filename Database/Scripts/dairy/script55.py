from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 55

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=mutton&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=1&nutrition.SUGAR.max=10

this script is for query 55, desserts in course, sugar value is medium, allowed allergy: dairy, mutton in allowed ingredient
there are no recipes for this query/combination
'''                  
