from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 2

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=394^Peanut-Free
&allowedDiet[]=388^Lacto vegetarian&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 2, main dishes in course , sugar value is high, allowed allergy: peanut, allowedDiet=lacto vegetarian;
no results returned
'''                  
                     
