from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 5
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free&allowedIngredient[]=pork
&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 5, Main Dishes in course, sugar value is High, allowed allergy: dairy, allowed ingredient:pork
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Slow-Cooker-Pork-Roast-2279611?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Asian_Style-Pork-Chops-Martha-Stewart?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/The-Pioneer-Woman_s-Pulled-Pork-2177948?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Spam-Musubi-1110828?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Honey-Dijon-Ham-2369352?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Cajun-Jambalaya-1499617?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Hawaiian-Pork-Chops-2215375?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Honey-Baked-Ham-1421394?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Ham-and-Beans-1015944?_app_id=dummyid&_app_key=dummykey']
    
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
    recipeData['allowedIngredient'] = ['pork']

    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

