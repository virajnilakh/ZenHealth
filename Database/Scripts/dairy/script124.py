from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 124

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=pork&allowedCourse[]=course^course-Soups&maxResult=10&nutrition.SUGAR.min=0&nutrition.SUGAR.max=1

this script is for query 124, soups in course , sugar value is low, allowed allergy: dairy, allowedDiet= Non vegetarian; allowedIngredient[]=pork
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Southern-Style-Cabbage-Soup-993907?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Bean-with-Bacon-Soup-1478766?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Kimchi-jjigae-_kimchi-pork-soup_-338914?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Slow-Cooker-Bacon-Corn-Chowder-1928085?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Great-Northern-Ham-_-Bean-Soup-2335478?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Turkey-Sausage_-Kale-and-White-Bean-Soup-2272477?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Wonton-Soup-472311?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/White-Bean-and-Kale-Soup-with-Chicken-Sausage-1476700?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/3-Ingredient-Corn-and-Bacon-Chowder-1843002?_app_id=dummyid&_app_key=dummykey'                     
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
    recipeData['sugarLevel'] = 'Low'
    recipeData['allowedIngredient'] = 'pork'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

