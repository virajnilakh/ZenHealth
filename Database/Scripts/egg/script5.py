from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 5

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=397^Egg-Free
&allowedIngredient[]=pork&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 5, main dishes in course , sugar value is high, allowed allergy: egg, allowedDiet=Non vegetarian; allowedIngredient[]=pork

no recipes retured for this query
'''                  
                     
