from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 17

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey
&allowedIngredient[]=beef&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 17, desserts in course , sugar value is high, allowed allergy: none, allowedDiet=Non Vegetarian; ['allowedIngredient']= 'beef' 
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Pizza-Bolognese-912521?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Mexikanische-Wrap---Pizza-806929?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Italienischer-Hackbraten-mit-saftiger-Fullung-und-Soe-919768?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Party-Moussaka-950770?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Low-Carb-_Oopsie_-Burger-918869?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Gefullte-Pfannkuchen-mit-Hackfleisch-Lauch-917142?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Sandras-Lahmacun-952370?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Pfannkuchen---Burger---Fricka-956985?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/American-Blueberry-Pancakes-948721?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedDiet'] = 'Non vegetarian'
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedAllergy'] = 'None'
    recipeData['allowedIngredient']= 'beef'
    
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

