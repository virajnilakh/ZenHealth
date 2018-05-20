from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 4
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free&allowedIngredient[]=beef
&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 4, Main Dishes in course, sugar value is High, allowed allergy: dairy, allowed ingredient:beef
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Oven-Barbecue-Brisket-2133470?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/One-Pan-Beef-Tenderloin-_-Roasted-Vegetables-2340712?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Korean-beef-Bulgogi-2171116?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Freezer-Friendly-Meal-1458906?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Grilled-Marinated-Flank-Steak-Simply-Recipes-42974?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Super-easy-slow-cooked-chili-304149?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Easy-Meatloaf-512120?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Best-Ever-Old-Fashioned-Meatloaf-2091486?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Crispy-Orange-Beef-1306414?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Irish-Stew-With-Guinness-_Pressure-Cooker_-2371749?_app_id=dummyid&_app_key=dummykey'
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
    #recipeData['Course'] = 'Main Dishes'
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedIngredient'] = ['beef']

    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

