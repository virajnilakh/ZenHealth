from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 63
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedDiet[]=389^Ovo%20vegetarian&allowedCourse[]=course^course-Main%20Dishes&maxResult=40&nutrition.SUGAR.min=1&nutrition.SUGAR.max=10

this script is for query 63, Main Dishes in course , sugar value is medium, allowed allergy: gluten, allowedDiet=Ovo vegetarian


'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Zucchini-Pasta-with-Vegan-Cashew-Basil-Pesto-2111849?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Black-Bean-and-Sweet-Potato-Enchiladas-681515?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Lentil-Chili-1208686?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Zucchini-with-lentils-and-roasted-garlic-308344?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Brazilian-Portabellas-2138770?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Lentil-Tacos-in-the-Slowcooker-2057421?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Mushroom-Paella-2040267?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Curried-Rice-and-Lentils-1722192?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Spaghetti-Squash-Curry-with-Roasted-Chickpeas-986493?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Samosa-Stir-fry-1264390?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/West-African-Peanut-Curry-with-Tofu-2029484?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/A-Complete-Vegan-Meal-2373705?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Spicy-Spaghetti-Squash-with-Black-Beans-2296557?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedDiet'] = 'Ovo vegetarian'
    recipeData['allowedAllergy'] = 'Gluten-Free'
    recipeData['sugarLevel'] = 'Medium'
    #recipeData['allowedIngredient'] = 'bacon'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

