from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 100

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedDiet[]=387^Lacto-ovo vegetarian&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=0&nutrition.SUGAR.max=1

this script is for query 100, lunch and snacks in course , sugar value is low, allowed allergy: dairy, allowedDiet=Lacto-ovo vegetarian ;

Grilled-Chicken-Sandwich-with-Avocado-and-Tomato-2258092
Chicken-Avocado-Burgers-1031197
Chicken-Avocado-Burgers-2402934

these were the recipes retured; so didn't populate db for this query
'''                  
                     
