from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 10
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=chicken&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 10, desserts in course, sugar value is High, allowed allergy: dairy, chicken in allowed ingrdient
no results/0 recipes for this query
'''

