from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 35

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=396^Dairy-Free
&allowedIngredient[]=bacon&allowedCourse[]=course^course-Breakfast and Brunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 35 , Breakfast and Brunch in course, sugar value is High, allowed allergy: dairy, bacon in allowed ingredient
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Southern-Butter-Beans-with-Bacon-2263683?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Bacon-Onion-wrapped-Meatball-Bombs-2020927?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Maple-Candied-Bacon-1436404?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Authentic-German-Potato-Salad-2088904?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Candied-Bacon-978243?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedIngredient'] = 'bacon'
   
        
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

