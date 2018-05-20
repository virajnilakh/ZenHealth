from firebase import firebase
import json
import requests
import os
from pprint import pprint

'''
Query1
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free&allowedDiet[]=390^Pescetarian
&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 1, Pescetarian diet, Main Dishes in course, sugar value is High, allowed allergy: dairy
'''

def getRecipeData():
    filePath = (os.path.join(os.getcwd(),"result.json"))
    if os.path.isfile(filePath):
        os.remove(filePath)
    recipeUrlList = ['http://api.yummly.com/v1/api/recipe/Zucchini-and-Green-Peas-Coconut-Curry-2281449?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/10-Minute-Maple-Crusted-Salmon-2209525?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Crispy-_-Chewy-Sesame-Shiitake-2187164?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Indian-Shrimp-Curry-2342556?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Thai-Sweet-Potato-Curry-2357881?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Swordfish-zucchini-kebabs-349125?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Crispy-honey-lime-tilapia-333373?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Maple-Glazed-Baked-Salmon-1564095?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Asian-Garlic-Tofu-2047342?_app_id=dummyid&_app_key=dummykey',
    'http://api.yummly.com/v1/api/recipe/Maple-Soy-Glazed-Salmon-2269949?_app_id=dummyid&_app_key=dummykey'
    ]
    
    
    for url in recipeUrlList:
        r = requests.get(url)
        data = r.json()
        extractDataFromUrl(filePath, data)
    
    
def extractDataFromUrl(filePath, data):
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
    #recipeData['Course'] = 'Main Dishes'
    recipeData['sugarLevel'] = 'High'
    
    pprint(recipeData)
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

