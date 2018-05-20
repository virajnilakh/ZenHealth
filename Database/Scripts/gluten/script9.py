from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 9

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedIngredient[]=mutton&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 9, main dishes in course , sugar value is low, allowed allergy: gluten, allowedDiet= Non vegetarian; allowedIngredient[]=mutton
no results
'''                  
                     
