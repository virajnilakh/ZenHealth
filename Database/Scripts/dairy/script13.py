from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 13
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=mutton&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

his script is for query 13, desserts in course, sugar value is High, allowed allergy: dairy, mutton in allowed ingrdient
no results/0 recipes for this query
'''

