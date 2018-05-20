from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 4

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=394^Peanut-Free
&allowedDiet[]=386^Vegan&allowedCourse[]=course^course-Main%20Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 4, main dishes in course , sugar value is high, allowed allergy: peanut, allowedDiet=vegan
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Eggplant-Onion-and-Tomato-Stew-_Vegan_-Gluten-Free_-Paleo-Friendly_-1278008?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Instant-Pot-Vegan-Pasta-Arrabiatta-Pasta-2414963?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Sticky-Sesame-Tofu-and-Broccoli-1686644?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Easy-Weeknight-Baked-Tofu-1186150?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Easy-french-ratatouille-308073?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Pasta-With-Caramelized-Onions_-Peas-And-Parsley-1318714?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Anti-Inflammatory-Smoothie-2034106?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/How-to-Can-Homemade-Salsa-2327684?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedDiet'] = 'Vegan'
    recipeData['allowedAllergy'] = 'Peanut-Free'
    recipeData['sugarLevel'] = 'High'
    #recipeData['allowedIngredient'] = 'mutton'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)

            
firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)
getRecipeData()

