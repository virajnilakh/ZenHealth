from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 52

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=chicken&allowedCourse[]=course^course-Desserts&maxResult=10&nutrition.SUGAR.min=1&nutrition.SUGAR.max=10

this script is for query 52, desserts in course, sugar value is medium, allowed allergy: dairy, chicken in allowed ingredient
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Mango-Chicken-Dog-Cookies-490603?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Hahnchen-aus-dem-Sack-914418?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Cupcakes-for-Chickens-561387?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Puppy-Cookies-_For-Dogs_-Food_com-148025?_app_id=dummyid&_app_key=dummykey'                     
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
    recipeData['allowedDiet'] = 'Non vegetarian'
    recipeData['allowedAllergy'] = 'Dairy-Free'
    recipeData['sugarLevel'] = 'Medium'
    recipeData['allowedIngredient'] = 'chicken'
        
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

