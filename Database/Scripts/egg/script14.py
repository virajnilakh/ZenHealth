from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 14

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=397^Egg-Free
&allowedIngredient[]=bacon&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 14, desserts in course , sugar value is high, allowed allergy: egg, allowedDiet=Non vegetarian; allowedIngredient[]=bacon

no recipes retured for this query
'''                  
                     
