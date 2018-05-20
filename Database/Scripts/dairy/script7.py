from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 7
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free&allowedIngredient[]=bacon
&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 7, Main Dishes in course, sugar value is High, allowed allergy: dairy, allowed ingredient:bacon
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Honey-Mustard-Chicken-1567234?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Sweet-Bacon-Wrapped-Chicken-Breasts-1393137?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Apricot-Glazed-Bacon-Wrapped-Cajun-Pork-Tenderloin-1910967?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Bacon-Wrapped-Honey-Mustard-Pork-Loin-1016657?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Apricot-Glazed-Bacon-Wrapped-Cajun-Pork-Tenderloin-2359552?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Crockpot-Hawaiian-Pizza-1769557?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Homemade-Slow-Cooker-Pork-and-Beans-1895610?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Plum-Chicken-with-Pistachio-685157?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Bacon-Wrapped-BBQ-Meatloaf-1185458?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Bacon-Wrapped-Salmon-with-Fruit-Chutney-1051170?_app_id=dummyid&_app_key=dummykey']
    
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
    #recipeData['Course'] = 'Main Dishes'
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedIngredient'] = ['bacon']

    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

