from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 68
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=pork&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=1&nutrition.SUGAR.max=10

this script is for query 68, Lunch in course , sugar value is medium, allowed allergy: dairy, allowedIngredient=pork

there are no recipes returned for this query
'''                  
                     
