from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 12
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=pork&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 12, desserts in course, sugar value is High, allowed allergy: dairy, pork in allowed ingredient, 
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Bacon-Fat-Peanut-Butter-Cookies-1571810?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Bacon-fat-gingersnaps-351370?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Gluten-Free-And-Dairy-Free-Mince-Pie-961639?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Bacon-fat-gingersnaps-360611?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Biscochitos-776352?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Chinese-Almond-Cookies-Recipezaar_6?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Pan-De-Polvo-Recipezaar_1?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Bacon-Fat-Spice-Cookies-774708?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Biscochitos-560507?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Grunkohlbrot-917179?_app_id=dummyid&_app_key=dummykey']
    
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
    recipeData['allowedDiet'] = 'Non Vegetarian'
    recipeData['allowedAllergy'] = 'Dairy-Free'
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedIngredient'] = 'pork'
    
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

