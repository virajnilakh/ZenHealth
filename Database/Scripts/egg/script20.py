from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 20

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=397^Egg-Free
&allowedIngredient[]=mutton&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 20, lunch in course , sugar value is high, allowed allergy: egg, allowedDiet=Non vegetarian; allowedIngredient[]=mutton

no recipes retured for this query
'''                  
                     
