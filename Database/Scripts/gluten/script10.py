from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 10

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedIngredient[]=bacon&allowedCourse[]=course^course-Main Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 10, main dishes in course , sugar value is low, allowed allergy: gluten, allowedDiet= Non vegetarian; allowedIngredient[]=bacon
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Crack-Potatoes-769586?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Green-Beans-and-Bacon-1188088?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedAllergy'] = 'Gluten-Free'
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedIngredient'] = 'bacon'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

