from firebase import firebase
import json
import requests
import os
from pprint import pprint
import pymongo


'''
Query 2

http://api.yummly.com/v1/api/recipes?_app_id=dummyid&_app_key=dummykey&allowedAllergy[]=393^Gluten-Free
&allowedDiet[]=388^Lacto%20vegetarian&allowedCourse[]=course^course-Main%20Dishes&maxResult=10&nutrition.SUGAR.min=10&nutrition.SUGAR.max=12

this script is for query 2, main dishes in course , sugar value is low, allowed allergy: gluten, allowedDiet= Lacto vegetarian
'''                  
                     
def getRecipeData():
    recipeUrlList = [
                     'http://api.yummly.com/v1/api/recipe/Pumpkin-Quinoa-Chili-2401625?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Thai-Peanut-Coconut-Cauliflower-Chickpea-Curry-2416469?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Easy-Cheese-Enchiladas-1290637?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Sour-Cream-Enchiladas-The-Pioneer-Woman-Cooks-_-Ree-Drummond-41194?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Butternut-Squash-and-Black-Bean-Enchilada-Skillet-1073856?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Quinoa-Stuffed-Red-Bell-Peppers-1392568?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Spicy-Butternut-Squash-Brown-Rice-Bowl-with-Cumin-Lime-Crema-2235553?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Spicy-White-Bean-Tomato-Skillet-2142681?_app_id=dummyid&_app_key=dummykey',
                     'http://api.yummly.com/v1/api/recipe/Mini-Lentil-Shepherd_s-Pies-2348845?_app_id=dummyid&_app_key=dummykey'
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
    recipeData['allowedDiet'] = 'Lacto vegetarian'
    recipeData['allowedAllergy'] = 'Gluten-Free'
    recipeData['sugarLevel'] = 'High'
    #recipeData['allowedIngredient'] = 'pork'
         
    print(recipeData ['Name'])
    
    result = firebase.post('/foodData', recipeData)
    print("RESULT IS:")
    print(result)
    

firebase = firebase.FirebaseApplication('https://zenhealth-215f6.firebaseio.com/', authentication=None)


getRecipeData()

