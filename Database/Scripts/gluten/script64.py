from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 64
http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedDiet[]=386^Vegan&allowedCourse[]=course^course-Main%20Dishes&maxResult=50&nutrition.SUGAR.min=1&nutrition.SUGAR.max=10

this script is for query 64, Main Dishes in course , sugar value is medium, allowed allergy: gluten, allowedDiet=vegan
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/World_s-Best-London-Broil-1081078?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Quinoa-Pizza-Crust-1121999?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Mujadarra-1223551?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Chickpea-Stew-_Vegan_-Gluten-free_-2199580?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Spicy-Vegetarian-Chili-Simply-Recipes-42632?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/26-Favorite-Cheap-and-Easy-Meals-1267279?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Sweet-Potato-Veggie-Burgers---Dairy-Free_-Gluten-Free_-Soy-Free_-Sugar-Free_-Egg-Free-2403393?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Vegan-lentil-chili-with-roasted-red-peppers_-olives_-and-green-onion-309276?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Tuscan-White-Beans-with-Spinach-1769892?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/A-Complete-Vegan-Meal-2170168?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Taco-Pasta-_glutenfree-_vegan-1183010?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/How-to-Make-Rajma-Dal-_Red-Kidney-Bean-Curry_-2216407?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedDiet'] = 'Vegan'
    recipeData['allowedAllergy'] = 'Gluten-Free'
    recipeData['sugarLevel'] = 'Medium'
    #recipeData['allowedIngredient'] = 'bacon'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

