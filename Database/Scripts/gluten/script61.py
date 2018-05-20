from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 61
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedDiet[]=390^Pescetarian&allowedCourse[]=course^course-Main%20Dishes&maxResult=30&nutrition.SUGAR.min=1&nutrition.SUGAR.max=10

this script is for query 61, Main Dishes in course , sugar value is medium, allowed allergy: gluten, allowedDiet=Pescetarian
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Shrimp-with-Zucchini-and-Tomatoes-1279810?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Cilantro-Lime-Tilapia-Tacos-2252905?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Oven-Poached-Salmon-with-Cherry-Tomatoes-and-Broccoli-_GF_-DF_-Paleo_-1519968?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Lighter-Eggplant-Parmesan-2401565?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Bangin-Good-Shrimp-2258094?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Pesto-Zucchini-Noodles-with-Shrimp-2040636?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Crock-Pot-Shrimp-and-Cheese-Grits-2121408?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Easy-Salmon-Kebabs-2065275?_app_id=dummyid&_app_key=dummykey'
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
        if (recipeData['Course'] == None):
            recipeData['Course'] = []
            recipeData['Course'].append("Main Dishes")
        recipeData['Cuisine'] = attrs.get('cuisine')
    else:
        recipeData['Course'] = "Main Dishes"
    recipeData ['Name'] = data.get('name')

    for nutrition in data['nutritionEstimates']:
        if nutrition['attribute'] == "ENERC_KCAL":
            if(nutrition['value'] is None):
                return
            nutritionData['Calories'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "SUGAR":
            if(nutrition['value'] is None):
                return
            nutritionData['Sugar'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "CHOCDF":
            if(nutrition['value'] is None):
                return
            nutritionData['Carbohydrates'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
    recipeData['Nutrients'] = nutritionData
    recipeData['allowedDiet'] = 'Pescetarian'
    recipeData['allowedAllergy'] = 'Gluten-Free'
    recipeData['sugarLevel'] = 'Medium'
    #recipeData['allowedIngredient'] = 'bacon'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

