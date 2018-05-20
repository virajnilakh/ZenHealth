from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 14
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=bacon&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 14, desserts in course, sugar value is High, allowed allergy: dairy, bacon in allowed ingredient

'Bacon-Fat-Peanut-Butter-Cookies-1571810',
               'Bacon-fat-gingersnaps-351370',
               'Bacon-fat-gingersnaps-360611',
               'Bacon-Fat-Spice-Cookies-774708'
The above 4 recipes for this cobination have been covered in query 12            
'''



