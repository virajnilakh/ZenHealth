from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 18
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free&allowedIngredient[]=beef
&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 18, lunch in course, sugar value is High, allowed allergy: dairy, beef in allowed ingredient 
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Sloppy-Joes-Recipe-only-3-ingredients_-2358218?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/The-Beef-Jerky-Recipe-_Almost_-Any-Guy-Can-Make-at-Home-2357181?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Sassy-Sloppy-Joes-2131172?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Sloppy-Joes-1737243?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Pulled-Pork-Sandwich-Simply-Recipes-42905?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Homemade-Beef-Jerky-A-Real-Convenient-Store-1893057?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Kimbap-334571?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Sloppy-Joe_s---Paleo-_-Whole30-1199314?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Sloppy-Joes-Recipe-only-3-ingredients_-1566430?_app_id=dummyid&_app_key=dummykey']
    
    for url in recipeUrlList:
        r = requests.get(url)
        data = r.json()
        extractDataFromUrl(data)
        
def extractDataFromUrl(data):
    recipeData = {}
    nutritionData = {}
    
    recipeData['Ingredients'] = data.get('ingredientLines')
    attrs = data.get('attributes')
    if attrs:
        recipeData['Course'] = attrs.get('course')
        recipeData['Cuisine'] = attrs.get('cuisine')
    recipeData ['Name'] = data.get('name')

    for nutrition in data['nutritionEstimates']:
        if nutrition['attribute'] == "ENERC_KCAL":
            nutritionData['Calories'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "SUGAR":
            nutritionData['Sugar'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "CHOCDF":
            nutritionData['Carbohydrates'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
    recipeData['Nutrients'] = nutritionData
    recipeData['allowedDiet'] = 'Non Vegeterian'
    recipeData['allowedAllergy'] = 'Dairy-Free'
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedIngredient'] = 'beef'
        
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

