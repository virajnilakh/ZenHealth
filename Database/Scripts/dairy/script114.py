from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 114

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedDiet[]=387^Lacto-ovo vegetarian
&allowedCourse[]=course^course-Breakfast and Brunch&maxResult=10&nutrition.SUGAR.min=0&nutrition.SUGAR.max=1

this script is for query 114, breakfast and brunch in course , sugar value is low, allowed allergy: dairy, allowedDiet= Lacto-ovo vegetarian;

Sauteed-Chicken-Breasts-In-Garlic-Olive-Oil-with-Mixed-Mushrooms-2403781 is the returned recipe: so did not populate
'''                  
                     
