from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 68
"http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedIngredient[]=pork&allowedCourse[]=course^course-Main%20Dishes&maxResult=20&nutrition.SUGAR.min=1&nutrition.SUGAR.max=10

this script is for query 68, Main Dishes in course , sugar value is medium, allowed allergy: gluten, allowedDiet=Non vegetarian; allowedIngredient[]=pork

Spinach-and-Gruyere-Cheese-Quiche-with-a-Hash-Brown-Crust-2179197
Greek-Style-Pork-Chops-1062107
Perfect-Pulled-Pork-1855071
Carnitas-Street-Tacos-2156175
Baked-Ribs-474749
CROCKPOT-PORK-CARNITAS-2148549
Creamy-BLT-Zucchini-Pasta-1693100
Slow-Cooker-Spicy-Gumbo-1688783
Beefy-Barbecue-Baked-Beans-2214333
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Spinach-and-Gruyere-Cheese-Quiche-with-a-Hash-Brown-Crust-2179197?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Greek-Style-Pork-Chops-1062107?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Perfect-Pulled-Pork-1855071?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Carnitas-Street-Tacos-2156175?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Baked-Ribs-474749?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/CROCKPOT-PORK-CARNITAS-2148549?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Creamy-BLT-Zucchini-Pasta-1693100?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Slow-Cooker-Spicy-Gumbo-1688783?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Beefy-Barbecue-Baked-Beans-2214333?_app_id=dummyid&_app_key=dummykey'                     
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
    recipeData['allowedIngredient'] = 'pork'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

