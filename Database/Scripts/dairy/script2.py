from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 2
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free&
allowedDiet[]=387^Lacto-ovo vegetarian&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 2, Lacto-ovo vegetarian diet, Main Dishes in course, sugar value is High, allowed allergy: dairy
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Moroccan-Inspired-Vegan-Quinoa-Chili-2369877?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Vegan-Irish-Stew-2175069?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Vegan-Mushroom-Paella-2374239?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Best-Homemade-Pizza-Dough-1005318?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Easy-BBQ-Tofu-440483?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/INDIAN-CHOLE-896576?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedDiet'] = 'Lacto-ovo vegetarian'
    recipeData['allowedAllergy'] = 'Dairy-Free'
    #recipeData['Course'] = 'Main Dishes'
    recipeData['sugarLevel'] = 'High'

    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

