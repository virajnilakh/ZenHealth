from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 67
"http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedIngredient[]=beef&allowedCourse[]=course^course-Main%20Dishes&maxResult=20&nutrition.SUGAR.min=1&nutrition.SUGAR.max=10

this script is for query 67, Main Dishes in course , sugar value is medium, allowed allergy: gluten, allowedDiet=Non vegetarian; allowedIngredient[]=beef
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Moroccan-Kefta-Kebab-2215753?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/5-Ingredient-Slow-Cooker-Steak-Fajitas-2101781?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Lemon-Garlic-Marinated-Flank-Steak-1687589?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Savory-Oven-Braised-Lamb-Shanks-2215619?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Coffee-_-Brown-Sugar-Rub-for-Wild-Game-1298586?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Marha-Porkolt---Hungarian-Beef-Paprika-Stew-2232755?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Garden-Skillet-2191738?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Hobo-Packets-2181856?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Slow-Cooker-Corned-Beef-and-Cabbage-1028240?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/One-Pot-Cabbage-Casserole-2266980?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Beef-Pot-Roast-769065?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Beef-Casserole-with-Shredded-Potato-Topping-2214706?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Keto-Beef-Stroganoff-2414370?_app_id=dummyid&_app_key=dummykey',
                     
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
    recipeData['allowedDiet'] = 'Non vegetarian'
    recipeData['allowedAllergy'] = 'Gluten-Free'
    recipeData['sugarLevel'] = 'Medium'
    recipeData['allowedIngredient'] = 'beef'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

