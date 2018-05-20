from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 3
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free&allowedIngredient[]=chicken
&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 3, Main Dishes in course, sugar value is High, allowed allergy: dairy, allowed ingredient:chicken
'''

def getRecipeData():
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Tomato-Basil-Chicken-Stew-2188027?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Chicken-Broccoli-and-Sweet-Potato-Sheet-Pan-Dinner-2201371?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Chicken-Zoodle-Pho-1544861?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Crispy-honey-lemon-chicken-333534?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Peach-chicken-345600?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Veri-Veri-Teriyaki-Grilled-Chicken-Kebabs-636795?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Grilled-Honey-Chili-Lime-Chicken-Thighs-2373632?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/BROWN-SUGAR-SPICED-BAKED-CHICKEN-622751?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Thai-Basil-Pork-_Gaprao-Moo-Kai-Daao_---Best-Ever_-2216851?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/20-Minute-Teriyaki-Chicken-_-Rice-1044470?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedIngredient'] = ['Chicken']

    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

