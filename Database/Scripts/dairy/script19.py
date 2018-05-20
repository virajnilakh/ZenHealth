from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 19
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free&allowedIngredient[]=pork
&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 19, lunch in course, sugar value is High, allowed allergy: dairy, pork in allowed ingredient 
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Peanut-Butter-Bacon-Smores-1258889?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Maple-Bacon-Kettle-Popcorn-482348?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Pinoy-Barbecue-599871?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/BLTA-Pesto-Chicken-Salad-1029014?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Poached-Egg-on-Toast-with-Chipotle-Mayonnaise_-Bacon-and-Avocado-Closet-Cooking-54924?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/BLT-Wraps-1338231?_app_id=dummyid&_app_key=dummykey'
    ]
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
    recipeData['allowedIngredient'] = 'pork'
        
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

