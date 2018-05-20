from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 6

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey
&allowedIngredient[]=chicken&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 6, Main Dishes in course , sugar value is high, allowed allergy: none, allowedIngredient[]=chicken; allowedDiet=Non vegetarian; 
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Southwestern-Chopped-Chicken-Salad-1720941?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Thai-Chicken-Meal-Prep-Bowls-with-Peanut-Sauce-2403314?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/BBQ-Bird-Dogs-2268361?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/How-to-Make-Homemade-Enchilada-Sauce-2350628?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/One-Pot-BBQ-Chicken-Pasta-2261019?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Instant-Pot-Chicken-and-Wild-Rice-Soup-2403351?_app_id=dummyid&_app_key=dummykey'                                    
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
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedAllergy'] = 'None'
    recipeData['allowedIngredient']= 'chicken'
    
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

