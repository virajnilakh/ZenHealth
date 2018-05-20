from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 121

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedDiet[]=387^ Lacto-ovo vegetarian&allowedCourse[]=course^course-Soups&maxResult=10&nutrition.SUGAR.min=0&nutrition.SUGAR.max=1

this script is for query 121, soups in course , sugar value is low, allowed allergy: dairy, allowedDiet= Lacto-ovo vegetarian

Spicy-Shrimp-Pho-1081964
Greek-Egg-Lemon-Soup-_Avgolemono-Soupa_-770797
Greek-Egg-and-Lemon-Soup-with-Chicken_-Brown-Rice_-and-Chickpeas-1384228
Easy-Homemade-Ramen-779567
Egg-Drop-Soup-2002516
Tonkotsu-Ramen-Broth-At-Home-2070723
Turkey-Sausage_-Kale-and-White-Bean-Soup-2272477
3-Ingredient-Corn-and-Bacon-Chowder-1843002
Slow-Cooker-Chicken-and-Wild-Rice-Soup-1902664
Sausage_-Kale_-and-Butternut-Squash-Soup-2224946

the above recipes are being returned for lacto voo vegeterian which is not right. since they contian meat: so didn't populate db for this
'''                  
                     
