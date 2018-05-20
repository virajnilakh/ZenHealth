from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 17
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=chicken&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 17, lunch in course, sugar value is High, allowed allergy: dairy, chicken in allowed ingredient 
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Chili-Lime-Baked-Chicken-Wings-1484894?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Quick-_-Easy-Chicken-Salad-Wraps--1470579?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/MINI-CHICKEN-SALAD-SANDWICHES-1534028?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Hot-_-sweet-chicken-wings-297272?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/BLT-Stuffed-Avocados-1494681?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Sweet-and-hot-wings-321321?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Strawberry-Chicken-Salad-with-Warm-Orange-Vinaigrette-486533?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/BLTA-Pesto-Chicken-Salad-Low-Carb_-Gluten-Free_-Paleo-2281703?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Santa-Fe-Chicken-Salad-1193471?_app_id=dummyid&_app_key=dummykey']
    
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
    recipeData['allowedIngredient'] = 'chicken'
        
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

