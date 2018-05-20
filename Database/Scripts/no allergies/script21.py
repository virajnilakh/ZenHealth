from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 21

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey
&allowedDiet[]=390^Pescetarian&allowedCourse[]=course^course-Lunch&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 21, Lunch and Snacks in course , sugar value is high, allowed allergy: none, allowedDiet=Pescetarian;  
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Nutty-breakfast-rolls-297269?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Banana-Snack-Muffins-for-Baby-2407435?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Borani-Banjan-_Afghan-Eggplant-Dish_-2180064?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Lisa_s-cross-cultural-salsa-with-tomato_-avocado_-lime_-and-feta-309201?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Crunchy-Garbanzo-Snacks-1063877?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Banana-bliss-breakfast-sandwiches-297581?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/No-Bake-Chai-Spiced-Date-Energy-Balls-2133902?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Vegan-Keto-Maple-Granola-Bars-_nut-free_-gluten-free_-soy-free_-2394515?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedDiet'] = 'Pescetarian'
    recipeData['sugarLevel'] = 'High'
    recipeData['allowedAllergy'] = 'None'
    #recipeData['allowedIngredient']= 'bacon'
    
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

