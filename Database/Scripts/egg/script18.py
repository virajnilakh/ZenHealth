from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 18

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=397^Egg-Free
&allowedIngredient[]=beef&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 18, lunch in course , sugar value is high, allowed allergy: egg, allowedDiet=Non vegetarian; allowedIngredient[]=beef
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Reuben-Sandwiches-997222?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedAllergy'] = 'Egg-Free'
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedIngredient'] = 'beef'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)

            
firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)
getRecipeData()

