from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 124
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=394^Peanut-Free
&allowedDiet[]=386^Vegan&allowedCourse[]=course^course-Main%20Dishes&maxResult=20&nutrition.SUGAR.min=0&nutrition.SUGAR.max=1

this script is for query 124, Main Dishes in course , sugar value is low, allowed allergy: peanut, allowedDiet=Vegan
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Oven-Roasted-Cabbage-Steaks-2229309?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Ten-Minute-Five-Ingredient-Black-Bean-Burgers-1119036?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Caribbean-Rice-And-Beans-1011774?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Avocado-Cream-Pasta-Sauce-1190200?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Best-Pizza-Dough-1024673?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Thin-Crust-Pizza-Dough-2295393?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/_Vegan_-Sun-Dried-Tomato-and-Chickpea-Burgers-2418777?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Arrabbiata-Pasta-1686610?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/All-Purpose-Lemon-_-Herb-Seafood-Marinade-2323519?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/My-Favorite-Baked-Tofu-2317817?_app_id=dummyid&_app_key=dummykey'
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
            nutritionData['Calories'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "SUGAR":
            nutritionData['Sugar'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
        if nutrition['attribute'] == "CHOCDF":
            nutritionData['Carbohydrates'] = str(nutrition['value']) + " " + nutrition['unit']['pluralAbbreviation']
    recipeData['Nutrients'] = nutritionData
    recipeData['allowedDiet'] = 'Vegan'
    recipeData['allowedAllergy'] = 'Peanut-Free'
    recipeData['sugarLevel'] = 'Low'
    #recipeData['allowedIngredient'] = 'bacon'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

