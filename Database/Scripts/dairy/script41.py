from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 41

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=mutton&allowedCourse[]=course^course-Soups&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 41 , soups in course, sugar value is High, allowed allergy: dairy, mutton in allowedIngredient

this query returns 0 recipes
'''                  

