from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 118

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=mutton&allowedCourse[]=course^course-Breakfast and Brunch&maxResult=10&nutrition.SUGAR.min=0&nutrition.SUGAR.max=1

this script is for query 118, Breakfast and Brunch in course , sugar value is low, allowed allergy: dairy, allowedDiet= Non vegetarian ;
allowedIngredient[]=mutton

no results returned
'''                  
            
