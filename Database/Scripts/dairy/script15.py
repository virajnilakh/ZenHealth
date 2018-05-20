from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 15
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedDiet[]=390^Pescetarian&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 15, lunch in course, sugar value is High, allowed allergy: dairy, pesceterian in allowed diet 
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Homemade-Granola-I-Adore-Food_-288929?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Chickpea-Nuggets-2149680?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Tuna-Salad-677005?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Chia-And-Flax-Seed-Biscuits-1067013?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Clean-Eating-Raw-Broccoli-Balls-_Raw_-Vegan_-Gluten-Free_-Dairy-Free_-Egg-Free_-Paleo-Friendly_-2362351?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Raw-Zucchini-Sushi-Rolls-1262398?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Baked-Beet-Chips-2075938?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Tortang-Talong-1111009?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Loaded-No-Bake-Peanut-Butter-Power-Bites-1540189?_app_id=dummyid&_app_key=dummykey']
    
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
    recipeData['allowedDiet'] = 'Pescetarian'
    recipeData['allowedAllergy'] = 'Dairy-Free'
    recipeData['sugarLevel'] = 'High'
        
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

